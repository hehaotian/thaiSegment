August 22, 2013

Language: Python 2.7.5

Approach: I mainly use for loop and if/elif statements to process the transitions of FST.

1. imports the sys library to set the default encoding to UTF-8 to make Thai readable.

2. uses the codecs to open the input file and split on new lines.

3. uses a for loop to read and process each character in Thai data.

4. uses the if/elif statements to process the transitions of FST, and adds up all the result as a text string.

5. writes the processed Thai text in the html form to an html file according to the html tags added to the original text.


Results:

คู่ แข่ง ขัน ต่าง ก็ คุม เชิง กัน 
เขา เงียบ ไป ครู่ หนึ่ง แล้ว พูด ขึ้น 
เธอ หัน มา คุ้ย ทราย ขึ้น มา ใหม่
ยิน ดี ที่ ได้ รู้ จัก คุ ณ
ฉัน เห็น เขา ตาม เธอ แจ ไป ทุก ที เป็น เงา ตาม ตัว ตลอด เลย
นก เล็ก มี หน้า อก สี แดง 
เจ้า ของ โรง งาน มอง หา ที่ ตั้ง ของ โรง งาน ใหม่
ขา ของ เขา สั่น เทา เมื่อ ต้อง ลง มา จาก ที่ สูง 
จุด สุด ยอด ของ ความ รู้ สึก ทาง เพ ศ
หนึ่ง หมื่น สอง พัน ห้า ร้อย หก สิบ สาม 
สอง หมื่น สี่ พัน หนึ่ง ร้อย ห้า สิบ สอง 
เขา เป็น เพื่อน ของ ฉัน มา หลาย ปี แล้ว
บ้าน หลัง นั้น ไม่ ใช่ ของ เขา เล็ก ไป
เขา ผลัด ค่า เช่า ห้อง มา เดือน หนึ่ง แล้ว
ฉัน ตาย ด้าน ใน เรื่อง ความ รัก เสีย แล้ว หลัง จาก ที่ ฉัน เคย ผิด หวัง กับ ความ รัก 
แบ่ง ขนม ปัง ก้อน หนึ่ง ออก เป็น สอง ชิ้น 
ใน หัว ใจ ของ ฉัน มี เพียง คุ ณ
วัน ที่ สี่ เดือน หน้า เป็น วัน พุ ธ
เมื่อ คืน นี้ ฉัน กลับ บ้าน ดึก มาก 
แต่ เรา ต้อง กลับ มา เปลี่ยน ชุด ก่อน 
เธอ รู้ สึก ใจ ชื้น ขึ้น เป็น กอง 
หมื่น สอง พัน สาม ร้อย สี่ สิบ ห้า
เขา เอา ช้าง บ้าน ไป ต่อ ช้าง ป่า
ฉัน เอง ไม่ ได้ พูด ดัง นั้น ดอก 
ขอ ให้ เดิน ทาง ด้วย ความ ปลอด ภัย
ดี ใจ ที่ ได้ รู้ จัก คุ ณ
ค่อย ชุบ ให้ เกิด ความ กล้า แข็ง 
หนัง เรื่อง นั้น ค่อน ข้าง น่า เบื่อ
เขา ไป ส่ง จด หมาย ให้ ผม
เขียน ด้วย มือ แล้ว ลบ ด้วย เท้า
รัก ฉัน ต้อง รัก หมา ฉัน ด้วย 
ราย งาน ข่าว กับ ที่ ได้ เห็น จริง ให้ ความ รู้ สึก ต่าง กัน มาก 
ถึง ตอน นี้ เรา ต้อง ยัก ย้าย ถ่าย เท เพื่อ เอา ตัว รอด แล้ว
ใบ ตอบ รับ ของ ผู้ ส่ง 
รอง เท้า หนัง สวม เดิน เล่น 
เครื่อง หมาย ทาง ข้าม โรง เรียน 
แป้น หมุน เครื่อง ปั้น ดิน เผา
ขี้ ผึ้ง ทา ริม ฝี ปาก 
เมื่อ สอง คืน ที่ ผ่าน มา
ไม่ ถูก บัง คับ ฝืน รั้ง 
แสง สี ขาว ของ กลุ่ม เม ฆ
ไม่ เก่า ครับ เพิ่ง สร้าง มา ได้ แค่ ห้า ปี เอง 
ฉัน เพิ่ง กลับ มา จาก เดิน เล่น ตาม ชาย หาด 
วัน นี้ ความ ขลัง ดัง กล่าว เริ่ม เสื่อม ลง แล้ว
ข่าว นี้ ได้ จาก แหล่ง ข่าว ที่ ไว้ ใจ ได้
ช่วย ย้าย กล่อง นี้ ไป ไว้ ที่ ห้อง นั้น หน่อย 
ชาว บ้าน ช่วย กัน ตาม หา เด็ก ที่ หาย ไป
แหล่ง ดึง ดูด นัก ท่อง เที่ยว 
งาน ที่ ได้ รับ มอบ หมาย 
นี่ คือ ถนน นั่น ใช่ ไหม
วัน นี้ ฉัน ไม่ ไป ไหน
ฉัน ไม่ ได้ เขียน จด หมาย 
เธอ ต้อง ขัด รอง เท้า ทั้ง หมด นี้
ปลุก ฉัน เวลา หก โมง เช้า ให้ ได้
ปลูก เรือน พอ ตัว หวี หัว พอ เกล้า
ต่าง กัน เหมือน ช้าง กับ ยุง 