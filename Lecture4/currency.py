import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    res = requests.get("https://api.frankfurter.dev/v1/latest", params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("ERROR:  API request unsuccessful")
    data = res.json()
    rate = data["rates"][other]
    #print(data)
    print(f"\n1 {base} is equal to {rate} {other}.")

if __name__ == "__main__":
    main()


# 200 OK
# 201 Created
# 400 Bad Request
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 422 Unprocessable Entity
# ...