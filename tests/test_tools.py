from mcp_server.server import calculator, get_current_time, memo, _memo_storage


class TestCalculator:
    def test_addition(self):
        assert "5" in calculator("2 + 3")

    def test_division(self):
        result = calculator("100 / 4")
        assert "25" in result

    def test_power(self):
        result = calculator("2 ** 10")
        assert "1024" in result

    def test_sqrt(self):
        result = calculator("sqrt(144)")
        assert "12" in result

    def test_invalid_expression(self):
        result = calculator("invalid")
        assert "오류" in result


class TestGetCurrentTime:
    def test_returns_time_string(self):
        result = get_current_time()
        assert "년" in result
        assert "월" in result
        assert "일" in result
        assert "요일" in result


class TestMemo:
    def setup_method(self):
        _memo_storage.clear()

    def test_read_empty(self):
        result = memo("read")
        assert "없습니다" in result

    def test_save_and_read(self):
        result = memo("save", "테스트 메모")
        assert "저장 완료" in result
        assert "1개" in result

        result = memo("read")
        assert "테스트 메모" in result

    def test_save_multiple(self):
        memo("save", "첫 번째")
        memo("save", "두 번째")
        result = memo("read")
        assert "첫 번째" in result
        assert "두 번째" in result

    def test_invalid_action(self):
        result = memo("delete")
        assert "알 수 없는" in result
