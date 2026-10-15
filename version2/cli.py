"""
交互式命令行入口（CLI）。

把 agent.py 的"单次任务循环"包进一个"能一直聊下去"的外层循环：
    - 每读一句话，就在同一份对话历史上跑一轮，因此上下文会累积，能多轮对话；
    - 每一轮的思考、工具调用、工具返回、最终回答都会实时打印出来。

运行：python cli.py
退出：输入 exit / quit / q（或按 Ctrl+D）
清空上下文：输入 reset
帮助：输入 help
"""

from agent import build_messages, create_client, run_turn

BANNER = """\
=======================================================
  Go2 LLM Agent —— 交互式命令行
  直接用中文下指令，和 Agent 对话。
  命令：exit 退出 | reset 清空上下文 | help 帮助
======================================================="""

HELP = """\
用法：
  直接输入自然语言，例如：
      去前面看看，然后告诉我电量
      向右转 90 度
  exit / quit / q   退出
  reset             清空对话上下文，重新开始
  help              显示本帮助"""


def main() -> None:
    print(BANNER)
    client = create_client()  # 整个会话共用一个客户端
    messages = build_messages()

    try:
        while True:
            try:
                user_input = input("\n你 > ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n再见。")
                break

            if not user_input:
                continue

            command = user_input.lower()
            if command in ("exit", "quit", "q"):
                print("再见。")
                break
            if command == "reset":
                messages = build_messages()
                print("[已清空上下文]")
                continue
            if command == "help":
                print(HELP)
                continue

            # 把这句话接进历史，然后在同一份历史上跑一轮
            messages.append({"role": "user", "content": user_input})
            run_turn(messages, client=client)
    finally:
        client.close()


if __name__ == "__main__":
    main()
