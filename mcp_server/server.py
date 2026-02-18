import math
import datetime
import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("python-mcp-server")

# ──────────────────────────────────────
# 메모 저장소 (서버가 켜져 있는 동안만 유지)
# ──────────────────────────────────────
_memo_storage: list[str] = []


@mcp.tool()
def calculator(expression: str) -> str:
    """수학 계산을 합니다.
    사칙연산, 거듭제곱, 제곱근 등을 지원합니다.
    예: '2 + 3', '100 / 7', 'math.sqrt(144)', '2 ** 10'
    """
    try:
        allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("_")}
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"계산 결과: {result}"
    except Exception as e:
        return f"계산 오류: {e}"


@mcp.tool()
def get_current_time() -> str:
    """현재 날짜와 시간, 요일을 알려줍니다."""
    now = datetime.datetime.now()
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    return (
        f"{now.strftime('%Y년 %m월 %d일')} "
        f"{weekdays[now.weekday()]}요일 "
        f"{now.strftime('%H시 %M분 %S초')}"
    )


@mcp.tool()
def memo(action: str, text: str = "") -> str:
    """메모를 저장하거나 읽습니다.
    action이 'save'면 메모를 저장하고, 'read'면 저장된 메모를 읽습니다.
    """
    if action == "save":
        _memo_storage.append(text)
        return f"메모 저장 완료! (총 {len(_memo_storage)}개)"
    elif action == "read":
        if not _memo_storage:
            return "저장된 메모가 없습니다."
        lines = [f"  {i + 1}. {m}" for i, m in enumerate(_memo_storage)]
        return "저장된 메모:\n" + "\n".join(lines)
    else:
        return f"알 수 없는 action: {action} ('save' 또는 'read'를 사용하세요)"


def main():
    transport = "stdio"
    if "--transport" in sys.argv:
        idx = sys.argv.index("--transport")
        if idx + 1 < len(sys.argv):
            transport = sys.argv[idx + 1]
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()
