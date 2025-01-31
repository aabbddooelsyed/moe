
#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>أوامر المشرفين ✅</u>**
**c** تعني  تشغيل في القناه.
/pause or /cpause • إيقاف تشغيل الموسيقى مؤقتا.
/resume or /cresume • استئناف الموسيقى المتوقفة مؤقتا.
/mute or /cmute • كتم صوت الموسيقى المشغلة.
/unmute or /cunmute • إلغاء كتم صوت الموسيقى الصامتة.
/skip or /cskip • تخطي تشغيل الموسيقى الحالية.
/stop or /cstop- إيقاف تشغيل الموسيقى.
/shuffle or /cshuffle • خلط قائمة التشغيل في قائمة الانتظار عشوائيا.
/seek or /cseek • إعادة توجيه البحث عن الموسيقى إلى المدة الخاصة بك
/seekback or /cseekback • إلى الوراء ابحث عن الموسيقى إلى المدة التي تقضيها
/restart • إعادة تشغيل بوت للدردشة الخاصة بك .


تخطي محدد ✅
/skip or /cskip [الرقم (مثال: 3)] 
    - يتخطى الموسيقى إلى رقم محدد في قائمة الانتظار. مثل: /skip 3 سوف تخطي الموسيقى إلى الموسيقى الثالثة في قائمة الانتظار وسوف تتجاهل الموسيقى 1 و 2 في قائمة الانتظار.

حلقة اللعب ✅
/loop or /cloop [تمكين/تعطيل] أو [أرقام بين 1-10] 
    - عند تنشيطه ، يقوم الروبوت بتكرار تشغيل الموسيقى الحالية إلى 1-10 مرات في الدردشة الصوتية. افتراضي إلى 10 مرات.

المستخدمون المصدقون ✅
المطرودين يمكن للمستخدمين استخدام أوامر المسؤول بدون حقوق المسؤول في الدردشة.

/auth - [معرف المستخدم] • إضافة مستخدم إلى قائمة المطرودين الخاصة بالمجموعة.
/unauth - [معرف المستخدم] • إزالة مستخدم من قائمة المطرودين للمجموعة.
/authusers - تحقق من قائمة المصادقة للمجموعة."""


HELP_2 = """✅<u>**أوامر التشغيل ✅**</u>
لأوامر المتوفرة = play , vplay , cplay

Force أوامر التشغيل = playforce , vplayforce , cplayforce

**c** اوامر تشغيل في القناه.

**v** لتشغيل   الفيديو.

force stands for force play.

/play or /vplay or /cplay  • سيبدأ Bot في تشغيل استعلامك المحدد على الدردشة الصوتية أو بث الروابط المباشرة على الدردشات الصوتية.

/playforce or /vplayforce or /cplayforce •  يؤدي فرض التشغيل إلى إيقاف مسار التشغيل الحالي في الدردشة الصوتية وبدء تشغيل المسار الذي تم البحث عنه على الفور دون إزعاج/مسح قائمة الانتظار.

/channelplay - [معرف القناه او ايدي القناه] أو [تعطيل] - يمكنك ربط القناة بمجموعة وبث الموسيقى على الدردشة الصوتية للقناة من مجموعتك.

✅**<u>قوائم تشغيل خادم البوت ✅</u>**
/playlist - تحقق من قائمة التشغيل المحفوظة على الخوادم.

/deleteplaylist - حذف أي موسيقى محفوظة في قائمة التشغيل

/play - ابدء تشغيل قائمة التشغيل المحفوظة من الخوادم."""

HELP_3 = """✅<u>**أوامر البوت ✅**</u>
/stats - احصل على أفضل 10 مسارات إحصائيات عالمية ، وأفضل 10 مستخدمين للبوت ، وأفضل 10 دردشات على الروبوت ، وأفضل 10 دردشات تم لعبها في دردشة وما إلى ذلك.

/sudolist - تحقق من قائمه المطورين.

/lyrics - [اسم الموسيقى] • يبحث في كلمات الأغاني عن موسيقى معينة على الويب.

/song - [اسم المسار] أو [رابط YT] • قم بتنزيل أي مسار من youtube بتنسيقات mp3 أو mp4.

/player -  احصل على لوحة تشغيل تفاعلية.

**c** تعني  تشغيل في القناه.

/queue or /cqueue • تحقق من قائمة انتظار الموسيقى."""

HELP_4 = """✅<u>**أوامر أضافية ✅**</u>
/start - بدء تشغيل بوت الموسيقى.

/help  - احصل على قائمة مساعد الأوامر مع تفسيرات مفصلة للأوامر.

/ping- بنك بوت والتحقق من ذاكرة الوصول العشوائي، وحدة المعالجة المركزية الخ احصائيات بوت.

✅<u>**أعدادات المجموعه ✅**</u>
/settings - للحصول على إعدادات كاملة للمجموعة باستخدام الأزرار المضمنة.

**الخيارات في الأعدادات ✅**
𝟏 يمكنك تعيين  جودة الصوت  التي تريد بثها على الدردشة الصوتية.

𝟐 يمكنك تعيين  جودة الفيديو  تريد البث على الدردشة الصوتية.

𝟑  مصادقة المستخدمين : - يمكنك تغيير وضع أوامر المسؤول من هنا إلى الجميع أو المسؤولين فقط. إذا كان الجميع ، فسيتمكن أي شخص موجود في مجموعتك من استخدام أوامر المسؤول (مثل /skip, /stop، إلخ)

𝟒  الوضع النظيف:  عند تمكينه ، يحذف رسائل الروبوت بعد 5 دقائق من مجموعتك للتأكد من أن الدردشة تظل نظيفة وجيدة.

𝟓 قيادة نظيفة : عند تنشيطه، سيقوم بوت بحذف الأوامر المنفذة (/play, /pause, /shuffle, /stop etc) فورا.

𝟔 اعدادات التشغيل:

/playmode - احصل على لوحة إعدادات تشغيل كاملة مع أزرار حيث يمكنك تعيين إعدادات تشغيل مجموعتك. 

<u>**الخيارات في وضع التشغيل ✅**:</u>
𝟏 وضع البحث [مباشر أو مضمن] • يغير وضع البحث أثناء تقديم /play مود. 

𝟐 أوامر المسؤول [الجميع أو المسؤولون] • إذا كان الجميع، فسيتمكن أي شخص موجود في مجموعتك من استخدام أوامر المسؤول (مثل /skip, /stop etc)

𝟑 نوع التشغيل [الجميع أو المشرفون] • إذا كان المسؤولون ، فيمكن للمسؤولين الموجودين في المجموعة فقط تشغيل الموسيقى على الدردشة الصوتية"""

HELP_5 = """🔰**<u>أضافة وازالة مطور :</u>**
/addudo - [اسم المستخدم أو الرد على مستخدم]
/delsudo - [اسم المستخدم أو الرد على مستخدم]

🛃**<u>هيروكو:</u>**
/usage - عدد ساعات الأستخدام.

🌐**<u>أضافة وحذف فار:</u>**
/get_var - احصل على var config من Heroku أو .env.

/del_var - احذف أي var على Heroku أو .env.

/set_var - [Var Name] [القيمة] - قم بتعيين Var أو تحديث Var على heroku أو .env. منفصلة Var وقيمتها مع مسافة.

🤖**<u>أوامر البوت:</u>**
/reboot - أعد تشغيل الروبوت الخاص بك.
/update - تحديث البوت.
/speedtest - تحقق من سرعات الخادم.
/maintenance - [enable تمكين / disable تعطيل].
/logger - [enable تمكين / disable تعطيل] يقوم البوت بتسجيل الاستعلامات التي تم البحث عنها في مجموعة المسجل.
/get_log - [Number of Lines] - احصل على سجل للروبوت الخاص بك من heroku أو vps. يعمل لكليهما.
/autoend - [تمكين | تعطيل] - تمكين إنهاء البث التلقائي بعد 3 دقائق إذا لم يكن هناك من يستمع.

📈**<u>أوامر الحالة:</u>**
/activevoice - تحقق من الدردشات الصوتية النشطة على الروبوت.
/activevideo - تحقق من مكالمات الفيديو النشطة على الروبوت.
/stats - تحقق من إحصائيات الروبوتات

⚠️**<u>وظيفة الدردشة فب القائمة السوداء:</u>**
/blacklistchat - [CHAT_ID] - ضع أي دردشة في القائمة السوداء من استخدام Music Bot
/whitelistchat - [CHAT_ID] - أضف أي دردشة بالقائمة السوداء إلى القائمة البيضاء من استخدام Music Bot
/blacklistedchat - تحقق من جميع الدردشات المدرجة في القائمة السوداء.

👤**<u>لحظر مستخدم:</u>**
/block - [اسم المستخدم أو الرد على مستخدم] - يمنع المستخدم من استخدام أوامر الروبوت.
/unblock - [اسم المستخدم أو الرد على مستخدم] - إزالة مستخدم من قائمة بوت المحظورة.
/blockusers - تحقق من قوائم المستخدمين المحظورة.

👤**<u>لمنع شخص من أستخدم البوت:</u>**
/gban - [اسم المستخدم أو الرد على مستخدم] - Gban مستخدمًا من الدردشة التي يقدمها الروبوت وأوقفه عن استخدام برنامج الروبوت الخاص بك.
/ungban - [اسم المستخدم أو الرد على مستخدم] - أزل مستخدمًا من قائمة gbanned في Bot واسمح له باستخدام برنامج الروبوت الخاص بك.
/gbannedusers - تحقق من قوائم المستخدمين Gbanned.

🎥**<u>وظيفة مكالمات الفيديو:</u>**
/set_video_limit - [عدد الدردشات] - قم بتعيين الحد الأقصى لعدد الدردشات المسموح بها لمكالمات الفيديو في كل مرة. افتراضي إلى 3 محادثات.
/videomode - [تنزيل | m3u8] - إذا تم تمكين وضع التنزيل ، فسيقوم الروبوت بتنزيل مقاطع الفيديو بدلاً من تشغيلها في شكل M3u8. افتراضيا إلى M3u8. يمكنك استخدام وضع التنزيل عندما لا يتم تشغيل أي استعلام في وضع m3u8.

⚡️**<u>وظيفة البوت الخاصة:</u>**
/authorize - [CHAT_ID] - اسمح بالمحادثة لاستخدام الروبوت الخاص بك.
/unauthorize - [CHAT_ID] - امنع الدردشة من استخدام الروبوت الخاص بك.
/authorized - تحقق من جميع الدردشات المسموح بها في برنامج الروبوت الخاص بك.

🌐**<u>وظيفة الأذاعة:</u>**
/broadcast - [رسالة أو رد على رسالة] - بث أي رسالة إلى الدردشات التي يقدمها الروبوت.
<u>خيارات البث:</u>
**-pin** : سؤدي الى بث رسالتك مع التثبيب.
**-pinloud** : سيؤدي الى بث رسالتك مع اشعار عالٍ.
**-user** : سيؤدي هذا إلى بث رسالتك للمستخدمين الذين بدأوا برنامج الروبوت الخاص بك.
**-assistant** : سيؤدي الى بث رسالتك من الحساب المساعد.
**-nobot** : سيؤدي هذا إلى إجبار الروبوت الخاص بك على عدم بث الرسالة.
**Example:** `/broadcast -user -assistant -pin Hello Testing`
"""
