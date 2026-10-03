import urllib.request


SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy"
]


def check_headers(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "SecurityHeaderChecker/1.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers

            print("\nURL:", url)
            print("Status:", response.status)
            print("\nSecurity Headers")
            print("----------------------------")

            for header in SECURITY_HEADERS:
                if headers.get(header):
                    print(f"[+] {header}: Present")
                else:
                    print(f"[-] {header}: Missing")

    except Exception as error:
        print("Could not check the URL.")
        print("Reason:", error)


def main():
    print("HTTP Security Header Checker")
    print("----------------------------")

    url = input("Enter a website URL: ").strip()

    if url:
        check_headers(url)
    else:
        print("Please enter a URL.")


if __name__ == "__main__":
    main()
