🎯 بازی شلیک به پهپاد (Bird Shooting Game)

یک بازی ساده و سرگرم‌کننده با استفاده از کتابخانه‌ی Pygame که در آن با ماوس به پهپادها شلیک می‌کنید و امتیاز می‌گیرید.

📷 پیش‌نمایش

(در صورت تمایل، یک تصویر یا گیف از بازی اجرا شده اینجا قرار دهید.)

🎮 نحوه‌ی بازی

نشانه‌ی تفنگ (Gun) با حرکت ماوس حرکت می‌کند.

با کلیک ماوس می‌توانید به پهپادها شلیک کنید.

به دو نوع پهپاد شلیک می‌کنید:

پهپاد معمولی (سمت چپ به راست) → امتیاز ۱

پهپاد دوم (سمت راست به چپ) → امتیاز ۲

اگر پهپادی از صفحه خارج شود و به آن شلیک نشده باشد، از بازی حذف می‌شود.

📁 فایل‌ها و منابع مورد نیاز

برای اجرای بازی مطمئن شوید که فایل‌های زیر در پوشه‌ی پروژه قرار دارند:

فایلتوضیحfirst drone image.pngتصویر پهپاد اولsecend drone image.pngتصویر پهپاد دومgun aim image .pngتصویر نشانه‌ی تفنگbackground image .jpgتصویر پس‌زمینه‌ی بازیgun sound .mp3صدای شلیک تفنگ

🛠 نصب و اجرا

1. نصب Pygame:



Copy code

pip install pygame 

2. اجرای بازی:

bash

Copy code

python game.py 

(نام فایل اسکریپت پایتون خود را مطابق با آنچه ذخیره کرده‌اید وارد کنید.)

💡 ایده‌های پیشنهادی برای ارتقاء

اضافه کردن صفحه‌ی پایان بازی یا Game Over.

محدود کردن زمان یا تعداد تیرها.

اضافه کردن صداهای برخورد یا انفجار.

نمایش بالاترین امتیاز (High Score).

تنظیم سطح سختی با گذر زمان.



🎯 Drone Shooting Game

A fun and simple 2D drone shooting game built using Pygame. Use your mouse to aim and shoot down drones flying across the screen. Try to get the highest score!

📸 Preview

(Insert a screenshot or GIF here if available)

🕹️ How to Play

Move your mouse to aim the gun.

Click the left mouse button to shoot.

Shoot down two types of drones:

Type 1 Drone (flies from left to right) → +1 point

Type 2 Drone (flies from right to left) → +2 points

If a drone escapes the screen, it disappears without affecting your score.

Your score is shown in the top-left corner.

📁 Required Assets

Make sure the following files are present in the same folder as your Python script:

File NameDescriptionfirst drone image.pngImage for the first dronesecend drone image.pngImage for the second dronegun aim image .pngGun crosshair imagebackground image .jpgBackground imagegun sound .mp3Shooting sound effect

🛠 Setup Instructions

1. Install Pygame

bash

Copy code

pip install pygame 

2. Run the Game

bash

Copy code

python game.py 

🚀 Features

Real-time mouse-controlled shooting

Sound effects on click

Scoreboard that updates in real-time

Two drone types with different behaviors

💡 Future Improvements (Optional Ideas)

Game Over screen or timer

High score saving system

Background music or explosion effects

Difficulty progression over time

Bullet count or ammo system
