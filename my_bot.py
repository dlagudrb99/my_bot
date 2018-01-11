import random
import discord
import time as t
from datetime import datetime
from discord.ext import commands
import threading
import hashlib

bot = commands.Bot(description="피난소 전용 봇(AS씹가능)", command_prefix="!")


@bot.event
async def on_ready():
    print('im ready! on shelter')


@bot.command()
async def cool(*, something):
    if something=="yokohama":
        await bot.say("제작자 까지마라")
    elif something=="요코하마":
        await bot.say("제작자 까지마라")
    elif something=="@yokohama" :
        await bot.say("멘션하지마라")
    elif something=="피난소 봇" :
        await bot.say("뭐라그랬냐?")
    elif something=="느금마" :
        await bot.say("뭐라그랬냐?")
    elif something=="완장" :
        await bot.say("뒤질래?")
    else:
        await bot.say("아니오,\""+something+"\"님은 병신입니다.")

@bot.command()
async def 갓겜판독기(*, something):
    if something=="롤":
        await bot.say("갓겜")
    elif something=="리그오브레전드":
        await bot.say("갓겜")
    elif something=="던전앤파이터":
        await bot.say("공익겜")
    elif something=="던파":
        await bot.say("공익겜")
    elif something=="히오스" :
        await bot.say("꺼져")
    elif something=="히어로즈오브더스톰" :
        await bot.say("꺼져")
    elif something=="배그" :
        await bot.say("갓겜")
    elif something=="배틀그라운드" :
        await bot.say("갓겜")
    elif something=="아르멜로" :
        await bot.say("꺼져")
    elif something=="디시트" :
        await bot.say("꺼져")
    elif something=="사막맵" :
        await bot.say("꺼져")
    elif something=="오버워치" :
        await bot.say("꺼져")
    elif something=="끄투" :
        await bot.say("우주갓겜")
    elif something=="젤다" :
        await bot.say("신포도")
    elif something=="닌텐도스위치" :
        await bot.say("닌스퍼거")
    elif something=="닌스" :
        await bot.say("닌스퍼거")
    elif something=="스플래툰" :
        await bot.say("수간충")
    elif something=="프메" :
        await bot.say("망함")
    elif something=="메이플스토리" :
        await bot.say("꺼져")
    elif something=="폴아웃" :
        await bot.say("갓갓갓3 똥오줌4")
    elif something=="커비" :
        await bot.say("진공바큠")
    elif something=="별의커비" :
        await bot.say("진공바큠")
    elif something=="귀네" :
        await bot.say("진공바큠")
    elif something=="메이플" :
        await bot.say("꺼져")
    elif something=="도타" :
        await bot.say("도슬람")
    elif something=="야생의숨결" :
        await bot.say("신포도")
    elif something=="서든어택" :
        await bot.say("난 자네가 꽤 맘에 들었었어")
    elif something=="허니셀렉트" :
        await bot.say("요직")
    elif something=="언더테일" :
        await bot.say("와!샌즈!파피루스!")
    elif something=="컵헤드" :
        await bot.say("와! 컵헤드 아시는구나!")
    elif something=="레인월드" :
        await bot.say("내가 이 작은 커뮤니티의 일부라니")
    elif something=="달껄룩" :
        await bot.say("내가 이 작은 커뮤니티의 일부라니")
    elif something=="소닉" :
        await bot.say("X")
    elif something=="록맨" :
        await bot.say("X")
    elif something=="데바데" :
        await bot.say("꺼져")
    elif something=="바둑" :
        await bot.say("갓파고")
    elif something=="체스" :
        await bot.say("틀딱쉰내나는겜 으으;")
    elif something=="리니지" :
        await bot.say("가챠겜")
    elif something=="로우바둑이" :
        await bot.say("갓겜")
    elif something=="와우" :
        await bot.say("틀딱")
    elif something=="월드오브워크래프트" :
        await bot.say("쉰내")
    elif something=="환세취호전" :
        await bot.say("틀니")
    elif something=="섯다" :
        await bot.say("우주갓겜")
    elif something=="마피아" :
        await bot.say("갓겜")
    elif something=="마크" :
        await bot.say("와! 도티! 잠뜰! 양띵!!!!")
    elif something=="마인크래프트" :
        await bot.say("와! 도티! 잠뜰! 양띵!!!!!!!!")
    elif something=="화이트데이" :
        await bot.say("복돌")
    elif something=="월탱" :
        await bot.say("고혈압")
    elif something=="포커" :
        await bot.say("갓겜")
    elif something=="글옵" :
        await bot.say("갓겜")
    elif something=="시즈" :
        await bot.say("갓겜")
    elif something=="칸코레" :
        await bot.say("네다씹")
    elif something=="캉코레" :
        await bot.say("네다씹")
    elif something=="소녀전선" :
        await bot.say("네다씹")
    elif something=="느금마" :
        await bot.say("뭐 씨발아?")
    elif something=="하스스톤" :
        await bot.say("대부분은 버그입니다")
    elif something=="페그오" :
        await bot.say("네다씹")
    elif something=="데드바이데이라이트" :
        await bot.say("꺼져")
    elif something=="GTA" :
        await bot.say("갓겜")
    elif something=="그타" :
        await bot.say("갓겜")
    elif something=="그타5" :
        await bot.say("갓겜")
    elif something=="스카이림" :
        await bot.say("갓겜")
    elif something=="아이마스" :
        await bot.say("네다씹")
    elif something=="러브라이브" :
        await bot.say("네다씹")
    elif something=="마구마구" :
        await bot.say("꺼져")
    elif something=="철권" :
        await bot.say("빠요엔")
    elif something=="뿌요뿌요" :
        await bot.say("원조집 빠요엔")
    elif something=="테트리스" :
        await bot.say("빠요엔")
    elif something=="스타" :
        await bot.say("네다틀")
    elif something=="포탈" :
        await bot.say("갓겜")
    elif something=="메탈슬러그" :
        await bot.say("이제 놓아줍시다")
    elif something=="지뢰찾기" :
        await bot.say("갓겜")
    elif something=="킹오파" :
        await bot.say("빠요엔")
    elif something=="테탑" :
        await bot.say("갓겜")
    elif something=="테이블탑시뮬레이터" :
        await bot.say("갓겜")
    elif something=="킹오브파이터즈" :
        await bot.say("빠요엔")
    elif something=="디아블로" :
        await bot.say("수면제")
    elif something=="바람의나라" :
        await bot.say("네다틀")
    elif something=="요코하마" :
        await bot.say("뭐 씨발아?")
    elif something=="yokohama" :
        await bot.say("뒤질래?")
    elif something=="스타크래프트" :
        await bot.say("네다틀")
    elif something=="완장" :
        await bot.say("뭐 씨발아?")
    elif something=="아르마" :
        await bot.say("네다틀")
    elif something=="포트리스" :
        await bot.say("네다틀")
    elif something=="붕괴3" :
        await bot.say("네다씹")
    elif something=="파이널판타지" :
        await bot.say("메갈")
    elif something=="파판" :
        await bot.say("메갈")
    elif something=="드래곤퀘스트" :
        await bot.say("네다틀")
    elif something=="트오세" :
        await bot.say("대부분은 버그입니다")
    elif something=="마비노기" :
        await bot.say("소꿉놀이")
    elif something=="마비노기영웅전" :
        await bot.say("꺼져")
    elif something=="마구마구" :
        await bot.say("교수점프캐치")
    elif something=="배틀필드" :
        await bot.say("배틀딱")
    elif something=="카트라이더" :
        await bot.say("갓겜")
    elif something=="바람의나라" :
        await bot.say("네다틀")
    elif something=="다크소울" :
        await bot.say("빠요엔")
    elif something=="디스아너드" :
        await bot.say("갓겜")
    elif something=="울펜슈타인" :
        await bot.say("갓겜")
    elif something=="워프레임" :
        await bot.say("꺼져")
    elif something=="제작자" :
        await bot.say("뒤질래?")
    elif something=="요코하마" :
        await bot.say("뒤질래?")
    else:
        await bot.say("좆듣보잡 들이밀고있네")

testdir = {"https://i.imgur.com/55OKj3V.png","https://i.imgur.com/Avfxs9a.png",
           "https://i.imgur.com/bnsqt9v.png","https://i.imgur.com/hQGCasJ.png",
           "https://i.imgur.com/jAduXWj.png","https://i.imgur.com/ay0Ggo0.png",
           "https://i.imgur.com/418VqdC.png","https://i.imgur.com/jAduXWj.png",
           "https://i.imgur.com/jXdevNx.png"}

testlist = list(testdir)


@bot.command()
async def 주사위():
        await bot.say("1~100 주사위 : {}".format(random.randint(1, 100)))

@bot.command()
async def IQ측정기():
        await bot.say("당신의 IQ는 {}입니다.".format(random.randint(60, 160)))

@bot.command()
async def iq측정기():
        await bot.say("당신의 IQ는 {}입니다.".format(random.randint(60, 160)))

@bot.command()
async def 케장콘(*, something):
    if something=="패드립":
        await bot.say(random.choice(testlist))
    elif something=="앗아아":
        await bot.say("https://i.imgur.com/0wI5uGB.png")
    elif something=="빳다죠":
        await bot.say("https://i.imgur.com/AaLjyje.png")
    elif something=="한남":
        await bot.say("https://i.imgur.com/zv7L5aF.png")
    elif something=="알파카":
        await bot.say("https://i.imgur.com/xvho2V0.png")
    elif something=="네다통":
        await bot.say("https://i.imgur.com/KrhkXnn.png")
    elif something=="감사":
        await bot.say("https://i.imgur.com/VQTjgVo.png")
    elif something=="조와용":
        await bot.say("https://i.imgur.com/iap5HyZ.png")
    elif something=="한심":
        await bot.say("https://i.imgur.com/E4O9KOR.png")
    elif something=="사이버망령":
        await bot.say("https://i.imgur.com/En0Wp0E.png")
    else:
        await bot.say("명령어 : 패드립, 한남, 알파카, 네다통, 앗아아, 감사, 조와용, 한심, 사이버망령")

@bot.command()
async def 히():
        await bot.say("데오코지마")

@bot.command()
async def 중붕이():
        await bot.say("병신들")

@bot.command()
async def 레후():
        await bot.say("레뺫")

@bot.command()
async def 데스():
        await bot.say("데챡")

@bot.command()
async def 테엥():
        await bot.say("마마..")

@bot.command()
async def 중갤():
        await bot.say("내가 이 작은 커뮤니티의 일부라니")

@bot.command()
async def 프니프니():
        await bot.say("마마..")

@bot.command()
async def 가로쉬():
        await bot.say("지글지글")

@bot.command()
async def 와():
        await bot.say("샌즈! 파피루스!")

@bot.command()
async def 짜잔():
        await bot.say("그런데 절대라는건 없군요")

@bot.event
async def on_message_delete(msg):
    print('======삭제기록감시자======')
    print((msg.author),(msg.timestamp))
    print(msg.content)
    print('==========================')

@bot.event
async def on_voice_state_update(before, after):
    t2 = t.localtime()
    print('======띵동기록감시자======')
    print('{}년{}월{}일{}시{}분{}초'.format(t2.tm_year, t2.tm_mon, t2.tm_mday, t2.tm_hour, t2.tm_min, t2.tm_sec))
    print(after.voice.voice_channel)
    print(before.name)
    print('==========================')

bot.run("Mzk1MDIzNDI1MTcwNzAyMzQ4.DSM10A.LV30L9ZoS3WNxnCbJUhRusLPjAk")
