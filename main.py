from py_near.account import Account
import asyncio


async def call_report_prices():

        # 输入 NEAR 账户 ID 和私钥
    accountId = "NEAR"
    privateKey = "ed25519:私钥"
    rpc = "https://rpc.mainnet.near.org"

    # 替换为你的测试网账户信息
    account = Account(accountId,privateKey,rpc)
    
    # 替换为您的 NEAR Token 合约地址
    sender = "inscription.near"
    method_name = "inscribe"
    method_args = {
        "p": "nrc-20",
        "op": "mint",
        "tick": "neat",
        "amt": "100000000"
    }

    
    # 执行合约方法调用
    result = await account.function_call(sender, method_name, method_args)
    
    print("Transaction Hash:", result.transaction.hash)

if __name__ == "__main__":
    # 运行异步函数多次
    for _ in range(1):
            # 获取正在运行的事件循环
        loop = asyncio.get_event_loop()
        loop.run_until_complete(call_report_prices())
        print("等待1秒...")
        loop.run_until_complete(asyncio.sleep(1))