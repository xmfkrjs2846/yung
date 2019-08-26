import discord
import time
import random
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(game=discord.Game(name="개발 중지ㅠ | help", type=1))

@client.event
async def on_message(message):
 if message.author != client.user:

    #융 대화
    if message.content.startswith("융"):
        await client.send_message(message.channel,"융융!")
    if message.content.startswith("혹시"):
        await client.send_message(message.channel,"흐.흐흐..!")
        await client.send_file(message.channel,'혹시.gif')
    if message.content.startswith("ㅋ"):
        await client.send_message(message.channel,"ㅋㅋㅋㅋㅋㅋ")
    if message.content.startswith("ㅗ"):
        await client.send_message(message.channel,"빡큐")
        time.sleep(2)
        await client.send_message(message.channel, "뽀큐! 뽁큐!")
        await client.send_message(message.channel, "빡큐 ㅗ^오^ㅗ")

    if message.content.startswith("야"):
        await client.send_message(message.channel,"응?! 나 불렀어??!")
        time.sleep(1)
        await client.send_message(message.channel,"미안.. 관심좀 끌어봤어;;")

    if message.content.startswith("https"):
        await client.send_message(message.channel,"머야?머야? 나도 볼래!!")
    if message.content.startswith("심심"):
        await client.send_message(message.channel,"휴가 나왔어? 부럽네~")
    if message.content.startswith("ㅇㅈ"):
        await client.send_message(message.channel, "저는 이거 인정 못합니다!!")
    if message.content.startswith("융털"):
        await client.send_message(message.channel, "벼...변.태..")
        await client.send_file(message.channel,'11111.gif')
    if message.content.startswith("ㅇㅈ"):
        await client.send_message(message.channel, "난 일단은 인정 해줄게~")
    if message.content.startswith("섹스"):
        await client.send_message(message.channel, "에!..엣.. 헤..헨따이!!")
    if message.content.startswith("시발"):
        await client.send_message(message.channel, "나쁜말? 나쁜말?! ㅡ.ㅡ")
    if message.content.startswith("ㄹㅇ"):
        await client.send_message(message.channel, "너어어..는 저어어어엉.말")
    if message.content.startswith("휴"):
        await client.send_message(message.channel, "뭔가 안좋은일이 라도 있었어??")
    if message.content.startswith("아님") or message.content.startswith("ㄴㄴ") or message.content.startswith("아니"):
        await client.send_message(message.channel, "머가 아닌데?? 솔직히 말해바~ 내가 다 들어줄게~ㅋㅋ")
        await client.send_file(message.channel, "아 아니야.gif")
    if message.content.startswith("오"):
        await client.send_file(message.channel, "나 살쪘나...gif")
    if message.content.startswith("메이플"):
        await client.send_message(message.channel, "일도 좋지만 좀 쉬어가면서 하는게 어때??!")
        await client.send_file(message.channel, "일.gif")
    if message.content.startswith("뜨끔") or message.content.startswith("들킴"):
        await client.send_message(message.channel, ".....?")
        await client.send_file(message.channel, "두리번 두리번")
    #호출
    if message.content.startswith('준혁'):
        myid = '<@379966497293991937>'
        await client.send_message(message.channel,"{}누군가 널 부르는거 같은데??".format(myid))
        await client.send_file(message.channel, "뜨끔...gif")
    if message.content.startswith('태훈'):
        myid='<@344788669502193666>'
        await client.send_message(message.channel, "{}누가 널 먹을려하는 것 같아 좀 무섭다.. ".format(myid))
    if message.content.startswith('대영'):
        myid='<@368617760412139520>'
        await client.send_message(message.channel, "{}아다 누가 너 부른다잉 씨게 대답 하그라!".format(myid))
    if message.content.startswith('영웅'):
        myid='<@286329350633029634>'
        await client.send_message(message.channel, "{}169.7cm..?그사람 여자야? 170cm가 안된다고?!".format(myid))
    if message.content.startswith('후석'):
        myid='<@247651944926019584>'
        await client.send_message(message.channel, "{}저..저기..어떡해 이사람 꼭 불러야해??ㅠㅠ".format(myid))
    if message.content.startswith('종민'):
        myid = '<@206663386937688065>'
        await client.send_message(message.channel, "{}리듬게임하고 있는 것 같은데 잠깐 나랑 이야기좀 해줄 수 있니?".format(myid))
    if message.content.startswith('민기'):
        myid = '<@253749865035726848>'
        await client.send_message(message.channel, "{}저기! 당신의 이름이 뜻하는건 뭔지 알려해주세요!!".format(myid))


    if message.content.startswith("안녕"):
        msg = "반가워~ {0.author.mention}아!!".format(message)
        await client.send_message(message.channel,"{}".format(msg))
        await client.send_file(message.channel,"새로운 안녕.gif")

        if message.content.startswith("골라"):
            choice = message.content.split(" ")
            chonumber = random.randint(1, len(choice) - 1)
            choiceresult = choice[chonumber]
            await client.send_message(message.channel, '나는 {}이게 좋은 것 같아!'.format(choiceresult))

        if message.content.startswith("주사위"):
            dice = random.randrange(1, 6)
            await client.send_message(message.channel, """너한테는 불행이 어울려보여~! 내가 3초 세줄게! 3초!""")
            time.sleep(1)
            await client.send_message(message.channel, "2초!")
            time.sleep(1)
            await client.send_message(message.channel, "1초!")
            time.sleep(1)
            await client.send_message(message.channel, "짜짠! 숫자 '{}이 나왔습니다!!".format(dice))

        if message.content.startswith('청소'):
            den = int(message.content[3:])
            if den > 0:
                async for m in client.logs_from(message.channel, limit=den + 1):
                    await client.delete_message(m)
                await client.send_message(message.channel, " 메세지 {}개를 청소했어! 잘했지?!".format(str(den)))
            else:
                await client.send_message(message.channel, "1개 이상의 메시지만 삭제할 수 있습니다!")

        if message.content.startswith('타이머'):
            Text = message.content[4:]
            sec = int(Text)
            for i in range(sec, 0, -1):
                await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : ' + str(i) + '초'))
                time.sleep(1)
            else:
                await client.send_message(message.channel,
                                          embed=discord.Embed(description='땡땡땡', colour=discord.Colour.gold()))

        if message.content.startswith("도와줘") or message.content.startswith("help"):
            channel = message.channel
            embed = discord.Embed(
                title="내가 할 수 있는 일들의 목록이야!",
                description="""잘 읽고 나한테 말해줘!! ------------------------------------------------------------""",
                colour=discord.Colour.blue()
            )

            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/405331598922219521/608627874299248661/151551155151511515.jpg')
            embed.add_field(name='융', value='융융이라 답해줍니다?', inline=False)
            embed.add_field(name='야', value='융이 대답을 해줍니다.', inline=False)
            embed.add_field(name='https', value='유튜브 영상에 감탄사를 해줍니다', inline=False)
            embed.add_field(name='안녕', value='융이 인사를 해줍니다', inline=False)
            embed.add_field(name='!융', value='!융 [질문]', inline=False)
            embed.add_field(name='주사위', value='1~6의 숫자를 골라줍니다', inline=False)
            embed.add_field(name='골라', value='골라 [고를꺼1] [고를꺼2] [고를꺼3] ...', inline=False)
            embed.add_field(name='ㅇㅈ', value='융이 인정을 안해줍니다ㅜ', inline=False)
            embed.add_field(name='인정', value='융이 인정을 해줍니다', inline=False)
            embed.add_field(name='청소', value='메세지를 삭제해줍니다. | 청소 (개수)', inline=False)
            embed.add_field(name='타이머', value='타이머 기능을 작동시킵니다 | 타이머 (초)', inline=False)
            await client.send_message(channel, embed=embed)

access_token = os.environ["봇 토큰"]

client.run(access_token)
