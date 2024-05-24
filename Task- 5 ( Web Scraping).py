import requests
from bs4 import BeautifulSoup
import csv

def get_page(url):
    """Fetch the content of the web page."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure the request was successful
    return response.text

def parse_product_page(html):
    """Parse the product page and extract product information."""
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    for product in soup.select('.product-item'):
        name = product.select_one('.product-name').get_text(strip=True)
        price = product.select_one('.product-price').get_text(strip=True)
        rating = product.select_one('.product-rating').get_text(strip=True)
        products.append({
            'name': name,
            'price': price,
            'rating': rating
        })

    return products

def save_to_csv(products, filename):
    """Save the product information to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price', 'rating'])
        writer.writeheader()
        writer.writerows(products)

def main():
    url = 'https://example-ecommerce.com/products'
    html = get_page(url)
    products = parse_product_page(html)
    save_to_csv(products, 'products.csv')
    print(f'Successfully saved {len(products)} products to products.csv')

if __name__ == "__main__":
    main()
