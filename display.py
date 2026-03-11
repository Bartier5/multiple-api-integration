from colorama import init,Fore,Style
from tabulate import tabulate

init(autoreset=True)

def display_crypto(crypto):
    if not crypto:
        print(Fore.RED + "  Crypto data unavailable")
        return
    rows = []
    for coin, values in crypto.items():
        change = values["change"]
        color = Fore.GREEN if change >= 0 else Fore.RED
        arrow = "▲" if change >= 0 else "▼"
        rows.append([
            coin.capitalize(),
            f"${values['price']:,.2f}",           # e.g. $65,000.12
            color + f"{arrow} {abs(change):.2f}%" # e.g. ▲ 2.34%
        ])
    headers = ["Coin", "Price (USD)", "24h Change"]
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))

def display_space(space):
    if not space:
        print(Fore.RED + "  Space data unavailable")
        return

    print(Fore.CYAN + Style.BRIGHT + f"  {space['title']}")
    print(Fore.WHITE + f"  Date: {space['date']}")
    print(Fore.WHITE + f"\n  {space['explanation']}")

def display_quote(quote):
    if not quote:
        print(Fore.RED + "  Quote unavailable")
        return

    print(Fore.YELLOW + f'  "{quote["text"]}"')
    print(Fore.WHITE  + f"  — {quote['author']}")
def display_errors(errors):
    if not errors:
        return
    print(Fore.RED + "\n  ⚠ Some sources failed:")
    for source, message in errors.items():
        print(Fore.RED + f"    • {source}: {message}")


def display_all(combined):
    print(Fore.CYAN + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.CYAN + Style.BRIGHT +   "      DAILY DASHBOARD   ")
    print(Fore.CYAN + Style.BRIGHT + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

    print(Fore.CYAN + Style.BRIGHT + "  💰 CRYPTO PRICES\n")
    display_crypto(combined["crypto"])

    print(Fore.CYAN + Style.BRIGHT + "\n  🚀 NASA SPACE FACT\n")
    display_space(combined["space"])

    print(Fore.CYAN + Style.BRIGHT + "\n  💬 QUOTE OF THE DAY\n")
    display_quote(combined["quote"])

    display_errors(combined["errors"])

    print(Fore.CYAN + Style.BRIGHT + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
