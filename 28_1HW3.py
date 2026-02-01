# המטרה: לקלוט גילאים של 10 שחקני חטיבת ביניים לקבוצת כדורסל
#
# כללים:
#
# בצע לולאה כדי לנסות לקלוט 10 גילאים
# אם הגיל קטן מ־12 – התעלם ממנו (לא סופר כשחקן תקין) והמשך ללולאה
# אם הגיל גדול מ־18 – צא מהלולאה עם break (זה "מבוגר מדי" לקבוצת נוער) מכיוון שעלולים לפסול את הקבוצה
# אחרת – הגיל תקין וספור אותו כשחקן תקין
# אחרי הלולאה, הדפס כמה שחקנים תקינים הצלחת לאסוף. וכמה שחקנים מעל גיל 16 ספרת

count = 0
overAged = 0

for i in range(10):
    age = int(input("Enter age: "))
    if age < 12:
        continue
    elif age > 18:
        print("Player too old")
        break
    else:
        count += 1
        if age > 16:
            overAged += 1

print("Valid Players:" , count)
print("Overaged Players:", overAged)
