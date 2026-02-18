# python-mcp-server

Python MCP(Model Context Protocol) 서버입니다. 계산기, 현재 시간, 메모 도구를 제공합니다.

## 도구 목록

| 도구 | 설명 |
|------|------|
| `calculator` | 수학 계산 (사칙연산, 거듭제곱, 제곱근 등) |
| `get_current_time` | 현재 날짜와 시간, 요일 |
| `memo` | 메모 저장/읽기 (in-memory) |

## 설치

```bash
pip install -e .
```

개발 의존성 포함:

```bash
pip install -e ".[dev]"
```

## 실행

### stdio 모드 (Claude Desktop 연동)

```bash
python -m mcp_server
```

### streamable-http 모드 (네트워크 접근)

```bash
python -m mcp_server --transport streamable-http
```

### MCP Inspector로 테스트

```bash
mcp dev mcp_server/server.py
```

## Claude Desktop 설정

`claude_desktop_config.json`에 아래 내용을 추가합니다:

```json
{
  "mcpServers": {
    "python-mcp-server": {
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/python-mcp-server"
    }
  }
}
```

> `cwd`를 프로젝트 경로로 변경하세요.

## 테스트

```bash
pytest
```
