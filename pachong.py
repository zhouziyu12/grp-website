import requests

# 图片URL
url = "https://www.nottingham.edu.cn/SiteElements/Images/2023-Revamp/Images/Homepage/Home-Traits-Cover-Mobile-800x800.jpg"

# 设置请求头（可选）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# 发送GET请求下载图片
try:
    response = requests.get(url, headers=headers)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 将图片内容写入文件
        with open("background.jpg", "wb") as file:
            file.write(response.content)
        print("Image downloaded successfully.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred while downloading the image: {e}")
