import httpx
import asyncio

async def verify():
    async with httpx.AsyncClient() as client:
        print("1. Testing Health Endpoint...")
        try:
            r = await client.get("http://127.0.0.1:8000/health")
            print(f"Health: {r.status_code}")
        except Exception as e:
            print(f"Failed to connect: {e}")
            return
            
        print("\n2. Simulating Situation -> Copilot Analysis...")
        payload = {
            "text": "A fight broke out near Gate C.",
            "matchday_context": {
                "phase": "Mid-Match"
            }
        }
        r = await client.post("http://127.0.0.1:8000/api/v1/copilot/analyze", json=payload, headers={"X-Demo-Token": "token_supervisor"})
        print(f"Analysis Status: {r.status_code}")
        data = r.json()
        print("Analysis Result:")
        print(data)
        
if __name__ == "__main__":
    asyncio.run(verify())
