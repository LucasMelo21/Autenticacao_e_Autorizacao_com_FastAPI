import httpx
import asyncio

BASE_URL = "http://127.0.0.1:8000/api/v1/usuarios"

async def test_api():
    async with httpx.AsyncClient() as client:
        signup_data = {
            "nome": "João",
            "sobrenome": "Silva",
            "email": "joao@email.com",
            "senha": "123456",
            "eh_admin": False
        }
        response = await client.post(f"{BASE_URL}/signup", json=signup_data)
        print("POST /signup")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")

        login_data = {
            "username": "joao@email.com",
            "password": "123456"
        }
        response = await client.post(f"{BASE_URL}/login", data=login_data)
        print("POST /login")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            token = response.json().get("access_token")
            print(f"Token: {token}\n")
        else:
            print(f"Response: {response.json()}\n")
            return

        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get(f"{BASE_URL}/", headers=headers)
        print("GET /usuarios")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")

        # 3. GET /logado - Usuário autenticado
        headers = {"Authorization": f"Bearer {token}"}
        response = await client.get(f"{BASE_URL}/logado", headers=headers)
        print("GET /logado")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")


if __name__ == "__main__":
    asyncio.run(test_api())