import pytest
from playwright.sync_api import sync_playwright

def test_check_website_encoding():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://qiita.com/KTakahiro1729/items/88f1da528b42f2740d14")  # ここにチェックしたいWebサイトのURLを入力してください
        content = page.content()
        browser.close()

        # コンテンツが正しくエンコードされているか（文字化けがないか）をチェックします
        assert "�" not in content

# テストを実行します
pytest.main(["-v", "-s", __file__])

