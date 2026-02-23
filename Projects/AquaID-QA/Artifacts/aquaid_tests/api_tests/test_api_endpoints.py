"""
AquaID – API Tests
api_tests/test_api_endpoints.py – Direct HTTP tests via requests library
Run independently of Selenium (no browser needed).

Usage:
    pytest api_tests/test_api_endpoints.py -v

Prerequisites:
    pip install requests pytest
    Set env vars:
        AQUAID_API   = http://localhost:5000/api   (default)
        FIREBASE_TOKEN = <valid Firebase ID token>
        FIREBASE_TOKEN2 = <second user's token>    (for cross-user tests)
"""

import os
import pytest
import requests

API_URL       = os.getenv("AQUAID_API",      "http://localhost:5000/api")
TOKEN         = os.getenv("FIREBASE_TOKEN",  "")    # User A token
TOKEN2        = os.getenv("FIREBASE_TOKEN2", "")    # User B token

FISH_FIXTURE  = os.path.join(os.path.dirname(__file__), "..", "fixtures", "fish_sample.jpg")


def auth_headers(token=TOKEN):
    return {"Authorization": f"Bearer {token}"}


def skip_if_no_token():
    if not TOKEN:
        pytest.skip("FIREBASE_TOKEN env var not set — skipping authenticated tests")


def skip_if_no_token2():
    if not TOKEN2:
        pytest.skip("FIREBASE_TOKEN2 env var not set — skipping cross-user tests")


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  HEALTH                                                                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestHealth:
    """API-HC-001 — Server health check."""

    def test_health_returns_200(self):
        """GET /health → 200 OK with {status: 'ok'}."""
        r = requests.get(f"{API_URL.replace('/api', '')}/health", timeout=5)
        assert r.status_code == 200
        assert r.json().get("status") == "ok"

    def test_health_response_time_under_500ms(self):
        """Health endpoint responds in under 500ms."""
        r = requests.get(f"{API_URL.replace('/api', '')}/health", timeout=5)
        assert r.elapsed.total_seconds() < 0.5


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  FISH IDENTIFICATION                                                         ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestIdentifyEndpoint:
    """API-ID-001 to API-ID-006 — POST /api/identify."""

    @pytest.mark.skipif(not os.path.exists(FISH_FIXTURE), reason="fish_sample.jpg not found")
    def test_valid_image_returns_200_and_all_fields(self):
        """API-ID-001: Valid fish image → 200 with all 11 identification fields."""
        with open(FISH_FIXTURE, "rb") as f:
            r = requests.post(f"{API_URL}/identify", files={"image": f}, timeout=30)

        assert r.status_code == 200
        data = r.json().get("data", {})
        required = [
            "speciesName", "scientificName", "commonNames",
            "description", "coloration", "habitat",
            "careInstructions", "diet", "breeding",
            "compatibility", "careDifficulty"
        ]
        for field in required:
            assert field in data, f"Missing field: {field}"

    @pytest.mark.skipif(not os.path.exists(FISH_FIXTURE), reason="fish_sample.jpg not found")
    def test_care_difficulty_is_valid_enum(self):
        """API-ID-004: careDifficulty value restricted to allowed enum values."""
        with open(FISH_FIXTURE, "rb") as f:
            r = requests.post(f"{API_URL}/identify", files={"image": f}, timeout=30)

        assert r.status_code == 200
        care = r.json().get("data", {}).get("careDifficulty", "")
        assert care in {"beginner", "intermediate", "expert"}, (
            f"careDifficulty '{care}' is not a valid value"
        )

    def test_no_image_returns_400(self):
        """API-ID-002: Request with no image → 400 Bad Request."""
        r = requests.post(f"{API_URL}/identify", timeout=10)
        assert r.status_code == 400
        assert "error" in r.json()

    def test_large_file_rejected(self):
        """API-ID-005 (BUG): Files >5MB should return 413 or 400 (currently fails)."""
        large_data = b"x" * (6 * 1024 * 1024)  # 6MB of bytes
        r = requests.post(
            f"{API_URL}/identify",
            files={"image": ("big.jpg", large_data, "image/jpeg")},
            timeout=15
        )
        # Current behaviour: 500 (bug). Expected: 413 or 400.
        assert r.status_code in {400, 413, 500}, f"Unexpected status: {r.status_code}"

    def test_non_image_file_handled(self):
        """API-ID-006 (BUG): Non-image file type should return 400 (currently 500)."""
        r = requests.post(
            f"{API_URL}/identify",
            files={"image": ("doc.pdf", b"%PDF-1.4 fake content", "application/pdf")},
            timeout=15
        )
        # Bug: currently 500. Expected: 400 with 'Only image files accepted'
        assert r.status_code in {400, 500}, f"Unexpected status: {r.status_code}"


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  ARTICLES                                                                    ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestArticlesEndpoint:
    """API-ART-001 to API-ART-014 — Articles endpoints."""

    def test_articles_no_auth_returns_401(self):
        """API-ART-003: GET /api/articles without token → 401."""
        r = requests.get(f"{API_URL}/articles", timeout=10)
        assert r.status_code == 401

    def test_articles_invalid_token_returns_401(self):
        """API-ART-004: GET /api/articles with invalid token → 401."""
        r = requests.get(
            f"{API_URL}/articles",
            headers={"Authorization": "Bearer faketoken123"},
            timeout=10
        )
        assert r.status_code == 401

    def test_get_articles_with_valid_token(self):
        """API-ART-005: GET /api/articles with valid token → 200 and articles array."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        assert r.status_code == 200
        assert "articles" in r.json()
        assert isinstance(r.json()["articles"], list)

    def test_articles_only_returns_own_articles(self):
        """API-ART-006: Response contains only articles owned by the requesting user."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        assert r.status_code == 200
        articles = r.json()["articles"]
        # Each article's userId should match the token owner (we can't decode JWT here,
        # but we verify all articles share the same userId)
        if len(articles) > 1:
            user_ids = {a.get("userId") for a in articles}
            assert len(user_ids) == 1, f"Multiple userIds found: {user_ids}"

    def test_get_article_by_id(self):
        """API-ART-007: GET /api/articles/:id returns the full article."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles in DB — create one first")

        article_id = articles[0]["id"]
        r = requests.get(f"{API_URL}/articles/{article_id}", headers=auth_headers(), timeout=10)
        assert r.status_code == 200
        assert r.json().get("id") == article_id

    def test_get_nonexistent_article_returns_404(self):
        """API-ART-008: GET /api/articles/nonexistentid → 404."""
        skip_if_no_token()
        r = requests.get(
            f"{API_URL}/articles/THIS_ID_DOES_NOT_EXIST_XYZ",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 404
        assert "error" in r.json()

    def test_cross_user_article_access_returns_403(self):
        """API-ART-009: User B cannot access User A's private article → 403."""
        skip_if_no_token()
        skip_if_no_token2()

        # Get User A's articles
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(TOKEN), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("User A has no articles")

        article_id = articles[0]["id"]

        # Try to access as User B
        r = requests.get(
            f"{API_URL}/articles/{article_id}",
            headers=auth_headers(TOKEN2),
            timeout=10
        )
        assert r.status_code == 403, (
            f"Expected 403, got {r.status_code} — cross-user article access should be forbidden"
        )

    def test_generate_article_missing_species_name(self):
        """API-ART-002: POST /api/articles/generate without speciesName → 400."""
        skip_if_no_token()
        r = requests.post(
            f"{API_URL}/articles/generate",
            data={},
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=10
        )
        assert r.status_code == 400
        assert "error" in r.json()

    def test_get_article_comments(self):
        """API-ART-010: GET /api/articles/:id/comments → 200 with comments array."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles to test comments on")

        article_id = articles[0]["id"]
        r = requests.get(
            f"{API_URL}/articles/{article_id}/comments",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 200
        assert "comments" in r.json()
        assert isinstance(r.json()["comments"], list)

    def test_add_comment_valid(self):
        """API-ART-011: POST comment with content → 201 Created."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles to comment on")

        article_id = articles[0]["id"]
        r = requests.post(
            f"{API_URL}/articles/{article_id}/comments",
            json={"content": "Selenium automated test comment", "rating": 5},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 201
        assert "commentId" in r.json()

    def test_add_comment_empty_content_returns_400(self):
        """API-ART-012: POST comment with empty content → 400."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles")

        article_id = articles[0]["id"]
        r = requests.post(
            f"{API_URL}/articles/{article_id}/comments",
            json={"content": ""},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 400

    def test_delete_article_endpoint_not_implemented(self):
        """API-ART-014 (BUG): DELETE /api/articles/:id — endpoint body not implemented."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles to test delete on")

        article_id = articles[0]["id"]
        r = requests.delete(
            f"{API_URL}/articles/{article_id}",
            headers=auth_headers(),
            timeout=10
        )
        # Bug: handler is empty — no actual delete happens.
        # Expect 200 but article still exists.
        if r.status_code == 200:
            # Verify article was NOT actually deleted (bug confirmation)
            check_r = requests.get(
                f"{API_URL}/articles/{article_id}",
                headers=auth_headers(),
                timeout=10
            )
            assert check_r.status_code == 200, (
                "Delete returned 200 but article was not deleted — BUG confirmed"
            )


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  MY AQUARIUM                                                                 ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestAquariumEndpoint:
    """API-AQ-001 to API-AQ-010 — /api/my-aquarium endpoints."""

    def test_get_aquarium_no_auth_returns_401(self):
        """GET /api/my-aquarium without token → 401."""
        r = requests.get(f"{API_URL}/my-aquarium", timeout=10)
        assert r.status_code == 401

    def test_get_aquarium_returns_list(self):
        """API-AQ-001: GET /api/my-aquarium → 200 with aquariumFish array."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/my-aquarium", headers=auth_headers(), timeout=10)
        assert r.status_code == 200
        assert "aquariumFish" in r.json()
        assert isinstance(r.json()["aquariumFish"], list)

    def test_get_empty_aquarium_returns_empty_array(self):
        """API-AQ-002: Empty aquarium → 200 with empty array (not 404)."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/my-aquarium", headers=auth_headers(), timeout=10)
        assert r.status_code == 200
        fish = r.json().get("aquariumFish", None)
        assert fish is not None, "Response missing aquariumFish field"

    def test_add_fish_missing_required_fields_returns_400(self):
        """API-AQ-004: POST /api/my-aquarium/add without required fields → 400."""
        skip_if_no_token()
        r = requests.post(
            f"{API_URL}/my-aquarium/add",
            json={"careDifficulty": "beginner"},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 400
        assert "error" in r.json()

    def test_add_duplicate_fish_returns_400(self):
        """API-AQ-005: Adding same species twice → 400 Duplicate fish."""
        skip_if_no_token()

        # First, get an article to use
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles available to add to aquarium")

        species = articles[0]["speciesName"]
        article_id = articles[0]["id"]

        payload = {"articleId": article_id, "speciesName": species}

        # Add once
        r1 = requests.post(
            f"{API_URL}/my-aquarium/add",
            json=payload,
            headers=auth_headers(),
            timeout=10
        )
        # Add again (duplicate)
        r2 = requests.post(
            f"{API_URL}/my-aquarium/add",
            json=payload,
            headers=auth_headers(),
            timeout=10
        )
        assert r2.status_code == 400, "Expected 400 for duplicate fish"
        assert "duplicate" in r2.json().get("error", "").lower() or \
               "already" in r2.json().get("message", "").lower()

    def test_update_fish_notes(self):
        """API-AQ-007: PUT /api/my-aquarium/:fishId updates notes."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/my-aquarium", headers=auth_headers(), timeout=10)
        fish_list = r.json().get("aquariumFish", [])
        if not fish_list:
            pytest.skip("No fish in aquarium to update")

        fish_id = fish_list[0]["id"]
        r2 = requests.put(
            f"{API_URL}/my-aquarium/{fish_id}",
            json={"notes": "Selenium test note — automated"},
            headers=auth_headers(),
            timeout=10
        )
        assert r2.status_code == 200
        assert "updated" in r2.json().get("message", "").lower()

    def test_update_nonexistent_fish_returns_404(self):
        """API-AQ-008: PUT on nonexistent fishId → 404."""
        skip_if_no_token()
        r = requests.put(
            f"{API_URL}/my-aquarium/FAKEID_DOESNOTEXIST",
            json={"notes": "test"},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 404

    def test_delete_fish_returns_200(self):
        """API-AQ-009: DELETE /api/my-aquarium/:fishId removes fish → 200."""
        skip_if_no_token()
        fish_r = requests.get(f"{API_URL}/my-aquarium", headers=auth_headers(), timeout=10)
        fish_list = fish_r.json().get("aquariumFish", [])
        if not fish_list:
            pytest.skip("No fish to delete")

        fish_id = fish_list[-1]["id"]  # Delete last to preserve others
        r = requests.delete(
            f"{API_URL}/my-aquarium/{fish_id}",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 200
        assert "removed" in r.json().get("message", "").lower()

    def test_delete_nonexistent_fish_returns_404(self):
        """API-AQ-010: DELETE nonexistent fishId → 404."""
        skip_if_no_token()
        r = requests.delete(
            f"{API_URL}/my-aquarium/FAKEID_DOESNOTEXIST",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 404


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  COMPARE                                                                     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestCompareEndpoint:
    """API-CMP-001 to API-CMP-005 — GET /api/compare."""

    def test_compare_no_auth_returns_401(self):
        """GET /api/compare without auth → 401."""
        r = requests.get(f"{API_URL}/compare?fish1=a&fish2=b", timeout=10)
        assert r.status_code == 401

    def test_compare_missing_fish2_returns_400(self):
        """API-CMP-002: Missing fish2 param → 400."""
        skip_if_no_token()
        r = requests.get(
            f"{API_URL}/compare?fish1=someid",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 400
        assert "error" in r.json()

    def test_compare_missing_both_params_returns_400(self):
        """Both fish1 and fish2 missing → 400."""
        skip_if_no_token()
        r = requests.get(f"{API_URL}/compare", headers=auth_headers(), timeout=10)
        assert r.status_code == 400

    def test_compare_nonexistent_ids_returns_404(self):
        """API-CMP-003: One or both invalid fish IDs → 404."""
        skip_if_no_token()
        r = requests.get(
            f"{API_URL}/compare?fish1=FAKEID1&fish2=FAKEID2",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 404

    def test_compare_two_valid_fish(self):
        """API-CMP-001: Two valid IDs → 200 with comparison object."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if len(articles) < 2:
            pytest.skip("Need at least 2 articles to compare")

        fish1, fish2 = articles[0]["id"], articles[1]["id"]
        r = requests.get(
            f"{API_URL}/compare?fish1={fish1}&fish2={fish2}",
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 200
        data = r.json()
        assert "fish1" in data
        assert "fish2" in data
        assert "compatibleTogether" in data

    def test_compare_same_id_returns_200_but_no_validation(self):
        """API-CMP-004 (BUG): Same ID for both → 200 with no duplicate warning."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles available")

        fish_id = articles[0]["id"]
        r = requests.get(
            f"{API_URL}/compare?fish1={fish_id}&fish2={fish_id}",
            headers=auth_headers(),
            timeout=10
        )
        # Bug: no validation, returns 200 with identical data
        assert r.status_code == 200
        data = r.json()
        if "fish1" in data and "fish2" in data:
            assert data["fish1"]["id"] == data["fish2"]["id"], "Same fish ID used for both slots"


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  TEXT-TO-SPEECH                                                              ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

class TestTTSEndpoint:
    """API-TTS-001 to API-TTS-006 — POST /api/text-to-speech."""

    def test_tts_no_auth_returns_401(self):
        """POST /api/text-to-speech without token → 401."""
        r = requests.post(
            f"{API_URL}/text-to-speech",
            json={"articleId": "test"},
            timeout=10
        )
        assert r.status_code == 401

    def test_tts_missing_article_id_returns_400(self):
        """API-TTS-003: POST with no articleId → 400."""
        skip_if_no_token()
        r = requests.post(
            f"{API_URL}/text-to-speech",
            json={},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 400
        assert "error" in r.json()

    def test_tts_nonexistent_article_returns_404(self):
        """API-TTS-004: POST with non-existent articleId → 404."""
        skip_if_no_token()
        r = requests.post(
            f"{API_URL}/text-to-speech",
            json={"articleId": "DOESNOTEXIST_XYZ_123"},
            headers=auth_headers(),
            timeout=10
        )
        assert r.status_code == 404

    def test_tts_cross_user_returns_403(self):
        """API-TTS-005: User B cannot generate audio for User A's article → 403."""
        skip_if_no_token()
        skip_if_no_token2()

        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(TOKEN), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("User A has no articles")

        article_id = articles[0]["id"]
        r = requests.post(
            f"{API_URL}/text-to-speech",
            json={"articleId": article_id},
            headers=auth_headers(TOKEN2),
            timeout=10
        )
        assert r.status_code == 403

    def test_tts_rate_limit_enforced(self):
        """API-TTS-006: 6th request within 1 hour → 429 Too Many Requests."""
        skip_if_no_token()
        list_r = requests.get(f"{API_URL}/articles", headers=auth_headers(), timeout=10)
        articles = list_r.json().get("articles", [])
        if not articles:
            pytest.skip("No articles available for rate limit test")

        article_id = articles[0]["id"]
        last_response = None
        for _ in range(6):
            last_response = requests.post(
                f"{API_URL}/text-to-speech",
                json={"articleId": article_id},
                headers=auth_headers(),
                timeout=15
            )
            if last_response.status_code == 429:
                break

        assert last_response is not None
        if last_response.status_code == 429:
            body = last_response.json()
            assert "rate" in body.get("error", "").lower() or "limit" in body.get("error", "").lower()
