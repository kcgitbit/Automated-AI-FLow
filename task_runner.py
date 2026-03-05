import schedule
import time

from product_engine.trend_crawler import fetch_trending_products
from product_engine.product_selector import select_best_product
from ai_content.copywriter import generate_marketing_copy
from ai_content.video_script import create_video_script
from media_generation.video_generator import generate_video
from social_automation.tiktok_poster import upload_tiktok


def full_pipeline():

    products = fetch_trending_products()

    product = select_best_product(products)

    copy = generate_marketing_copy(product)

    script = create_video_script(product)

    video = generate_video(script)

    upload_tiktok(video)

    print("Pipeline complete")


schedule.every().day.at("10:00").do(full_pipeline)


def run():

    while True:

        schedule.run_pending()

        time.sleep(5)
