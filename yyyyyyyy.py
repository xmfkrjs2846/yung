from bs4 import BeautifulSoup as bs
import requests
import discord
import time
import random
import os
import asyncio
from datetime import datetime, timedelta

client = discord.Client()
talk = [0]

ROLE = "에엣취"
ROLE1 = "메이플안하는사람"
준혁1 = int(379966497293991937)
태훈1 = int(344788669502193666)
대영1 = int(368617760412139520)
영웅1 = int(286329350633029634)
후석1 = int(247651944926019584)
종민1 = int(206663386937688065)
민기1 = int(253749865035726848)
권영1 = int(410450620823371778)
성현1 = int(245857392623878146)
시원1 = int(519867402385752064)
종원1 = int(271957069991641088)
희태1 = int(241906227611697153)
성규1 = int(356311092332593152)
강성1 = int(386501875379470338)

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("ready")
    game = discord.Game("New Game!!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    msg = "메이플이 모야! 서버에 온걸 환영해 <@{}>야~".format(str(member.id))
    channel = discord.utils.get(member.guild.channels, id=int("527835129150832641"))
    await channel.send('{}'.format(msg))
    await channel.send(
                              embed=discord.Embed(colour=discord.Colour.gold(), title='신입?! 이런 채널에?? 헐....;;'))
    await asyncio.sleep(1)
    await channel.send("나는 기능하고 회화적인 부분을 도와줄꺼야")
    await asyncio.sleep(1)
    await channel.send("아오바는 음악적인 부분을 도와줄꺼야")


@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, id=int("527835129150832641"))
    msg = '<@{}>가 퇴사했어! 정말 현명한 선택인 것 같아.'.format(str(member.id))
    await channel.send('{}'.format(msg))


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("퇴근"):
            if message.content[0:] == '퇴근':
                await message.channel.send("수고하셨어요~! 저 먼저 퇴근할게요!\n(앞으로 융이 아무 말도 하지 않습니다)",file=discord.File('퇴근.gif'))
                del talk[0]
                talk.append(1)
                game = discord.Game("집에서 노는 것을")
                await client.change_presence(status=discord.Status.dnd, activity=game)

        if message.content.startswith("출근"):
            await message.channel.send("아아..내 황금같은 주말이 벌써..\n(융이 작동을 시작합니다.)",file=discord.File('출근.jpg'))
            del talk[0]
            talk.append(0)
            game = discord.Game("New Game!!")
            await client.change_presence(status=discord.Status.online, activity=game)

        if talk[0] == 0:
            if message.content.startswith("융"):
                await message.channel.send("융융!")

            if message.content.startswith("혹시"):
                await message.channel.send("흐..흐흐..", file=discord.File('혹시.gif'))

            if message.content.startswith("ㅋ"):
                await message.channel.send("ㅋㅋㅋㅋㅋㅋ")

            if message.content.startswith("ㅗ"):
                await message.channel.send("빡큐")
                await asyncio.sleep(2)
                await message.channel.send("뽀큐! 뽁큐!")
                await message.channel.send("빡큐 ㅗ^오^ㅗ")

            if message.content.startswith("야"):
                await message.channel.send("응?! 나 불렀어??!")
                asyncio.sleep(1)
                await message.channel.send("미안.. 관심좀 끌어봤어;;")

            if message.content.startswith("http"):
                await message.channel.send("머야?머야? 나도 볼래!!")

            if message.content.startswith("집가고싶다"):
                await message.channel.send("ㅋㅋㅋㅋ 나는 평생 노는데 부럽지? 부러럽지?? 부럽지???!")

            if message.content.startswith("심심"):
                await message.channel.send('너도 심심하냐..후우..', file=discord.File('심심.gif'))

            if message.content.startswith("ㅇㅈ") or message.content.startswith("인정"):
                injun = ["저기 이건 내가 생각하기에 좀 아니라도 생각하는데...",
                         "너 의외로 맞는 말 한다?!"]
                hey1 = random.choice(injun)
                await message.channel.send("{}".format(hey1))

            if message.content.startswith("ㄷㅊ") or message.content.startswith("닥쳐"):
                await message.channel.send("선배 죄송합니다...ㅜㅜ 다시 일 시작할게요ㅠㅠ 해고만은!!")

            if message.content.startswith("바보"):
                await message.channel.send("너한테 바보라는데? 풉!", discord.File("바보.jpg"))

            if message.content.startswith("이이잉"):
                await message.channel.send("앗살라말라이꿈~", discord.File("안경.png"))
            if message.content.startswith("섹스") or message.content.startswith("ㅅㅅ"):
                await message.channel.send("???!")
                await asyncio.sleep(1)
                await message.channel.send("??", file=discord.File('머야.gif'))
            if message.content.startswith("시발") or message.content.startswith("ㅅㅂ"):
                await message.channel.send("나쁜말? 나쁜말?! ㅡ.ㅡ")

            if message.content.startswith("ㄹㅇ"):
                await message.channel.send("너어어..는 저어어어엉.말")

            if message.content.startswith("밥"):
                await message.channel.send("나도 배고프다..")
                await message.channel.send("아..오늘 머먹을까??")
            if message.content.startswith("휴"):
                if message.content[0:] == '휴':
                    await message.channel.send("뭔가 안좋은일이 라도 있었어??")

            if message.content.startswith("아님") or message.content.startswith("ㄴㄴ") or message.content.startswith("아니"):
                await message.channel.send("머가 아닌데?? 솔직히 말해바~ 내가 다 들어줄게~ㅋㅋ")

            if message.content.startswith("안됨") or message.content.startswith("안돼"):
                await message.channel.send("안되는거 시러!", file=discord.File('시러.gif'))
                await message.channel.send("안되는거 시러!")
                await message.channel.send("시러!!")
                await message.channel.send("시러!!!")
                await asyncio.sleep(2)
                await message.channel.send("미안 내가 좀 어떻게 됬었나봐...")

            if message.content.startswith("메이플"):
                await message.channel.send("또 메이플이야..? 이제 슬슬 질릴때가 된거 같은데")
            if message.content.startswith("롤"):
                await message.channel.send("나도 롤할래~ 끼워줘")

            if message.content.startswith("?"):
                await message.channel.send(file=discord.File('두리번.gif'))

            if message.content.startswith("병신") or message.content.startswith("ㅂㅅ") or message.content.startswith("ㅄ"):
                await message.channel.send("....???")
                await asyncio.sleep(1)
                await message.channel.send("아! 뭔지 알았어~! ㅂㅅ인지 검증해볼게~!")
                await asyncio.sleep(2)
                answer1 = ["삐비빅 넌 몸이 아픈걸로 판정났어! 병원이라도 가봐~!",
                           "칫! 널 바보 취급 할 수 있는 기회였는데 정상이라니..."]
                hey = random.choice(answer1)
                await message.channel.send("{}".format(hey))

            if message.content.startswith("역겹") or message.content.startswith("ㄴㄷㅆ") or message.content.startswith(
                    "네다씹") or message.content.startswith("무서"):
                await message.channel.send("나랑 3M만 떨어줘줄래? 조끔 그렇다..",file=discord.File('무서.jpg'))

            if message.content.startswith("힘내") or message.content.startswith("화이팅"):
                await message.channel.send("아자아자", file=discord.File("아자.jpg"))
            # 호출
            if message.content.startswith('준혁'):
                myid = '<@379966497293991937>'
                await message.channel.send("{}??").format(myid))
                await asyncio.sleep(1)
                await message.channel.send("그는 이제 없어~")
                await asyncio.sleep(2)
                await message.channel.send("내가 먹어버렸거든~♡")
            if message.content.startswith('태훈'):
                myid = '<@344788669502193666>'
                await message.channel.send("{}누군가 널 부르는거 같은데??".format(myid))
            if message.content.startswith('대영'):
                myid = '<@368617760412139520>'
                
                await message.channel.send("{}아다 누가 너 부른다잉 씨게 대답 하그라!".format(myid))
            if message.content.startswith('영웅'):
                myid = '<@286329350633029634>'
               
                await message.channel.send("{}169.6cm..? 풉?! 그..그게..혹시 키말하는 거야??! ㅋㅋ".format(myid))
            if message.content.startswith('후석'):
                myid = '<@247651944926019584>'
               
                await message.channel.send("{}저..저기..어떡해 이사람 꼭 불러야해??ㅠㅠ".format(myid))
            if message.content.startswith('종민'):
                myid = '<@206663386937688065>'
                
                await message.channel.send("{}리듬게임하고 있는 것 같은데 잠깐 나랑 이야기좀 해줄 수 있니?".format(myid))
            if message.content.startswith('민기'):
                myid = '<@253749865035726848>'
               
                await message.channel.send("{}저기! 당신의 이름이 뜻하는건 뭔지 알려주세요!!".format(myid))
            if message.content.startswith('권영'):
                myid = '<@410450620823371778>'
               
                await message.channel.send("{}통신보안 통신보안! 권영이를 호출중~".format(myid))
            if message.content.startswith('현개') or message.content.startswith("성현"):
                myid = '<@245857392623878146>'
               
                await message.channel.send("{}혀어어어어어언언언언개개객개개개".format(myid))
            if message.content.startswith('시원'):
                myid = '<@519867402385752064>'
               
                await message.channel.send("{}야~ 도박좀 그만하고 다녀라.... 글고 렙좀 올려".format(myid))
            if message.content.startswith('종원'):
                myid = '<@271957069991641088>'
               
                await message.channel.send("{}아이돌마스터?? 그게 머야? 먹는거야? 그리고 혹시 러브라이브 좋아해??!ㅋ".format(myid))
            if message.content.startswith('희태'):
                myid = '<@241906227611697153>'
               
                await message.content.send("{}벌레다!! 꺅!.. 서..선배.. 저 벌레좀 어떻게 해주세요!ㅠㅠ ".format(myid))
            if message.content.startswith('성규') or message.content.startswith('슬기') or message.content.startswith('성구'):
                myid = '<@356311092332593152>'
               
                await message.channel.send("{} 550만원 쓴 음머어~ 찾아요!!".format(myid))
            if message.content.startswith("안녕") or message.content.startswith("ㅎㅇ"):
                if message.content[0:] == '안녕':
                    msg = "반가워~ {0.author.mention}아!!".format(message)
                    await message.channel.send(file=discord.File('새로운 안녕.gif'))
                    await message.channel.send("{}".format(msg))
            if message.content.startswith('강성'):
                myid = '<@386501875379470338>'
                me = message.guild.get_member(강성1)
                msg = "{0.author.mention}이가 부르고있어 어서 대답해주는게 좋을 것 같은데?".format(message)
                await me.send("{}".format(msg))
                await message.channel.send("{}저기 메이플 대체 언제 그만 두실 꺼에요?!".format(myid))
            if message.content.startswith('전역준혁'):
                lasttime = datetime(2022, 7, 10, 0, 0, 0)
                firsttime = datetime.now()
                time2 = (lasttime-firsttime).days
                await message.channel.send("아마 {}일 정도?? 남은 것 같아~".format(time2))
            if message.content.startswith("!융"):
                msgg = message.content[3:]
                answer = [
                    '그게 좋은거같아!',
                    '나 그거 완전 좋아',
                    '그게 먼데 난 처음듣는건데??',
                    '흐헤헤 이거 치워줘 ㅜㅜ',
                    '넌 미움받을 짓만 하는구나..',
                    '아무생각 없다',
                    '(딴청을 피우는 것 같다']
                total = random.choice(answer)
                people = '{0.author.mention}'.format(message)
                await message.channel.send('{}의 질문:{}\n융의 대답:{}'.format(people, msgg, total))
            if message.content.startswith('날씨'):
                search = message.content[3:]
                html = requests.get('https://search.naver.com/search.naver?query={} 날씨'.format(search))
                soup = bs(html.text, 'html.parser')

                data1 = soup.find('ul', {'class': 'info_list'})
                data3 = data1.find('p', {'class': 'cast_txt'}).text
                data2 = soup.find('p', {'class': 'info_temperature'})
                data4 = data2.find('span', {'class': 'todaytemp'}).text

                data5 = soup.find('div', {'class': 'tomorrow_area'})
                data6 = data5.find('p', {'class': 'info_temperature'})
                data8 = data6.find('span', {'class': 'todaytemp'}).text
                data7 = data5.find('ul', {'class': 'info_list'}).text

                tomorrowAreaBase = soup.find('div', {'class': 'tomorrow_area'})
                tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
                tomorrowAfter1 = tomorrowAllFind[1]
                tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
                tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
                tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 온도
                tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
                tomorrowAfterValue = tomorrowAfterValue1.text.strip()  # 날씨
                await message.channel.send('현재 {}의 온도는 {}˚이며\n날씨는 {}'.format(search, data4, data3))
                await message.channel.send(
                                          '--------------------------\n내일 오전의 온도는 {}˚이며\n날씨는 {}'.format(data8, data7))
                await message.channel.send(
                                          '--------------------------\n내일 오후의 온도는 {}˚이며\n날씨는 {}'.format(
                                              tomorrowAfterTemp, tomorrowAfterValue))
                await asyncio.sleep(1)
                await message.channel.send('-----------------------\n이상 이글점프소속 그래피커 이이지마 윤이였습니다!!')

            if message.content.startswith("골라"):
                choice = message.content.split(" ")
                chonumber = random.randint(1, len(choice) - 1)
                choiceresult = choice[chonumber]
                await message.channel.send('나는 "{}" 좋다고 생각해!!'.format(choiceresult))
            if message.content.startswith("전해"):
                axcy = message.content[3:]
                await message.channel.purge(limit=1)
                await message.channel.send("{}".format(axcy))
            if message.content.startswith("주사위"):
                dice = random.randrange(1, 6)
                await message.channel.send("""너한테는 불행이 어울려보여~! 내가 3초 세줄게! 3초!""")
                await asyncio.sleep(1)
                await message.channel.send("2초!")
                await asyncio.sleep(1)
                await message.channel.send("1초!")
                await asyncio.sleep(1)
                await message.channel.send("짜짠! 숫자 '{}이 나왔습니다!!".format(dice))

            if message.content.startswith('청소'):
                clear = message.content.split(" ")
                if int(clear[1]) == 0:
                    await message.channel.send("나하고 놀고싶다는거야??\n0으로 입력되었어 다시 확인해바")
                elif int(clear[1]) > 99:
                    await message.channel.send("너무 많은 양은 내가 처리할 수 없어\n내 능력 부족이다..")
                else:
                    clears = clear[1]
                    await message.channel.purge(limit=int(clears)+1)
                    await message.channel.send("{}개의 작업을 처리했어~!\n나 잘했지??! ㅋㅋ".format(int(clears)))

            if message.content.startswith("조용"):
                name2 = message.content.split(" ")
                name3 = name2[1]
                name4 = name3[3:21]
                name5 = int(name4)
                member = message.channel.guild.get_member(user_id=name5)
                role = discord.utils.get(message.guild.roles, name=ROLE)
                role1 = discord.utils.get(message.guild.roles, name=ROLE1)
                await member.add_roles(role)
                await member.remove_roles(role1)
            if message.content.startswith("취소"):
                name2 = message.content.split(" ")
                name3 = name2[1]
                name4 = name3[3:21]
                name5 = int(name4)
                member = message.channel.guild.get_member(user_id=name5)
                role = discord.utils.get(message.guild.roles, name=ROLE)
                role1 = discord.utils.get(message.guild.roles, name=ROLE1)
                await member.add_roles(role1)
                await member.remove_roles(role)

            if message.content.startswith('검색'):
                life = message.content[3:]
                learn = life.split(" ")
                vrsize = len(learn)  # 배열크기
                vrsize = int(vrsize)
                encText = learn[0]
                for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
                    encText = ('{}+{}'.format(encText, learn[i]))
                html1 = ('https://search.naver.com/search.naver?query={}'.format(encText))
                html4 = ('https://www.youtube.com/results?search_query={}'.format(encText))
                html2 = (
                    'https://www.google.com/search?biw=1920&bih=969&ei=2pClXdu9DdXemAWLkKyoDw&q={}&oq={}&gs_l=psy-ab.3..0l10.60853.65724..65879...12.0..3.219.2223.8j11j1......0....1..gws-wiz.....0..0i67j0i131j0i10j0i10i30j0i5i10i30.EV6bS6ZxCD8&ved=0ahUKEwjbkpes-Z3lAhVVL6YKHQsIC_UQ4dUDCAs&uact=5'.format(
                        encText, encText))
                encText1 = learn[0]
                for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
                    encText1 = ('{}%20{}'.format(encText1, learn[i]))
                html3 = ('https://namu.wiki/w/{}'.format(encText1))
                naver = ('네이버_링크')
                tree = ('나무위키_링크')
                google = ('구글_링크')
                youtu = ('유튜브_링크')
                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/621324300120490006/633613406150328320/155151515151.jpg')
                embed.add_field(name='네이버,구글,나무위키,유튜브사이트로 검색할게~!',
                                value='{}를 검색해볼게~\n-------------------------------------------------------'.format(
                                    life), inline=False)
                embed.add_field(name='네이버', value='[%s](<%s>)' % (naver, html1), inline=False)
                embed.add_field(name='구글', value='[%s](<%s>)' % (google, html2), inline=False)
                embed.add_field(name='나무위키', value='[%s](<%s>)' % (tree, html3), inline=False)
                embed.add_field(name='유튜브', value='[%s](<%s>)' % (youtu, html4), inline=False)
                embed.set_footer(
                    icon_url='https://cdn.discordapp.com/attachments/621324300120490006/631109608638906408/12121212121211111.jpg',
                    text=f'{message.author.name}아 우리 쉬는시간을 가지는건 어때??')
                await message.channel.send(embed=embed)
            if message.content.startswith('운세'):
                Point = random.randint(1, 100)
                if Point >= 95:
                    await message.channel.send("{}의 운세는 '대길'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour.gold(),
                                                                                   title='오늘 도박이라도 해보는게 어때?ㅋㅋ'))
                elif Point >= 85:
                    await message.channel.send(
                                              "{}의 운세는 '길'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour.gold(),
                                                                                   title='흐음 오늘 좋은 일이 생길 수도??'))
                elif Point >= 75:
                    await message.channel.send(
                                              "{}의 운세는 '중길'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour.gold(),
                                                                                   title='흐음 오늘 좋은 일이 생길 수도??'))
                elif Point >= 65:
                    await message.channel.send(
                                              "{}의 운세는 '소길'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(), title=' 나름..? 나쁘지 않네'))
                elif Point >= 45:
                    await message.channel.send(
                                              "{}의 운세는 '평'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(), title='평..범..해...시시하다'))
                elif Point >= 35:
                    await message.channel.send(
                                              "{}의 운세는 '흉'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(), title=' 헤에에..'))
                elif Point >= 25:
                    await message.channel.send(
                                              "{}의 운세는 '소흉'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(),
                                                                  title='오늘 발밑 보고 조심히 다녀~ㅋㅋ'))
                elif Point >= 15:
                    await message.channel.send(
                                              "{}의 운세는 '반흉'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(),
                                                                  title='당신은 반흉이요!!! 위이위이 저리가시오!'))
                elif Point >= 5:
                    await message.channel.send(
                                              "{}의 운세는 '말흉'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(),
                                                                  title='나한테 붙지마!! 흉 옮겠다...'))
                elif Point <= 5:
                    await message.channel.send(
                                              "{}의 운세는 '대흉'이며,\n행운수치는 100/{}입니다.".format(message.author.name, Point))
                    await message.channel.send(
                                              embed=discord.Embed(colour=discord.Colour.gold(),
                                                                  title='너...오늘..집에 가만히..있어.. 좀 불안해~'))

            if message.content.startswith('이미지검색'):
                search = message.content[6:]
                html = requests.get(
                    'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(search))
                soup = bs(html.text, 'html.parser')
                imgs = soup.find('img', class_='_img')
                imgs2 = imgs.get('data-source')

                link = soup.find('div', {'class': 'photo_grid _box'})
                link2 = link.findAll('a')
                link3 = link2[1]
                link4 = link3.get('href')

                embed = discord.Embed(
                    colour=discord.Colour.green()
                )
                embed.add_field(name='검색: ' + search, value='이미지링크 : ' + link4, inline=False)
                embed.set_footer(
                    icon_url='https://cdn.discordapp.com/attachments/621324300120490006/631109608638906408/12121212121211111.jpg',
                    text=f'{message.author.name}선배가 요청하신 자료에요~ 저 잘했죠?!')
                embed.set_image(url=imgs2)  # 이미지의 링크를 지정해 이미지를 설정합니다.
                await message.channel.send(embed=embed)  # 메시지를 보냅니다.

            if message.content.startswith("메이플지지"):
                abritudy = message.content.split(" ")
                namereal = abritudy[1]
                htmll = requests.get('https://maple.gg/u/{}'.format(namereal))
                maplegg = 'https://maple.gg/'
                soup = bs(htmll.text, 'html.parser')
                maple = soup.find('section', {'class': 'container'})
                maple1 = maple.find('div', {'class': 'col-lg-8'})
                maple2 = maple1.find('img')['alt']  # 서버
                maple21 = maple1.find('b').text  # 이름
                maple3 = maple1.find('ul')
                maple4 = maple3.find('li').text  # 레벨
                maple5 = maple3.findAll('li')
                maple6 = maple5[1].text  # 직업
                maple7 = maple5[2]
                maple8 = maple7.findAll('span')
                maple9 = maple8[1].text  # 인기도
                maple10 = maple1.find('div', {'class': 'row'})
                try:
                    maple11 = maple10.find('a').text  # 길드
                except AttributeError:
                    maple11 = 'X'
                    print('길드없음')
                maple12 = maple10.find('span').text
                maple13 = maple12.split("\n")
                maple14 = maple13[0]  # 종합랭킹
                maple15 = maple10.findAll('span')
                maple16 = maple15[1].text  # 월드랭킹
                maple17 = maple15[2].text  # 직업랭킹
                picture = maple.find('img')
                picture1 = picture.get('src')
                embed = discord.Embed(colour=discord.Colour.green())
                embed.set_thumbnail(url=picture1)
                embed.add_field(name='메이플지지로 검색중~~',
                                value='{}를 검색해볼게~\n-------------------------------------------------------'.format(
                                    namereal),
                                inline=False)
                embed.add_field(name='검색결과',
                                value='시버: %s\n닉네임: %s\n%s\n직업: %s\n인기도: %s\n길드: %s\n종합랭킹:%s\n월드랭킹:%s\n직업랭킹(월드): %s' % (
                                maple2, maple21, maple4, maple6, maple9, maple11, maple14, maple16, maple17),
                                inline=False)
                embed.add_field(name='자세히는 직접 검색해줘~', value='%s' % (maplegg), inline=False)
                embed.set_footer(
                    icon_url='https://cdn.discordapp.com/attachments/621324300120490006/631109608638906408/12121212121211111.jpg',
                    text=f'{message.author.name}너?! 메이플 경력좀 있는데?!')
                await message.channel.send(embed=embed)

            if message.content.startswith("재획"):
                await message.channel.send("30분쿠폰 4개는 '1'\n그외는 '2'를 입력시켜줘~")
                def pred(m):
                    return m.author == message.author and m.channel == message.channel
                msg = await client.wait_for('message', check=pred)
                if msg.content == '1':
                    await message.channel.send("1번이 선택 되었습니다.\n5초후 시작합니다.", delete_after=2)
                    await asyncio.sleep(5)
                    await message.channel.send("{0.author.mention}재물획득의 비약을 시작중~!!".format(message))
                    await message.channel.send("{0.author.mention}아 1번째 30분 쿠폰을 먹어야해".format(msg), delete_after=5)
                    await asyncio.sleep(1800)
                    await message.channel.send("{0.author.mention}아 2번째 30분 쿠폰을 먹어야해".format(msg), delete_after=5)
                    await asyncio.sleep(1800)
                    await message.channel.send("{0.author.mention}아 3번째 30분 쿠폰을 먹어야해".format(msg), delete_after=5)
                    await asyncio.sleep(1800)
                    await message.channel.send("{0.author.mention}아 4번째 30분 쿠폰을 먹어야해".format(msg), delete_after=5)
                    await message.channel.send("{0.author.mention} 1재획 수고했어~".format(msg))
                if msg.content == '2':
                    await message.channel.send("경험치 쿠폰을 입력해줘\n ex: 30 30 20 20, 20 20 20 20 20 20\n")
                    def pred(m):
                        return m.author == message.author and m.channel == message.channel
                    msg1 = await client.wait_for('message', check=pred)
                    if msg1.content[0:2] == "20" or msg1.content[0:2] == "30" or msg1.content[0:2] == "15" or msg1.content[0:2] == "10" or msg1.content[0:2] == "60":
                        exp = msg1.content.split(" ")
                        try:
                            axp1 = int(exp[0]) * 60
                        except IndexError:
                            axp1 = 0
                        try:
                            axp2 = int(exp[1]) * 60
                        except IndexError:
                            axp2 = 0
                        try:
                            axp3 = int(exp[2]) * 60
                        except IndexError:
                            axp3 = 0
                        try:
                            axp4 = int(exp[3]) * 60
                        except IndexError:
                            axp4 = 0
                        try:
                            axp5 = int(exp[4]) * 60
                        except IndexError:
                            axp5 = 0
                        try:
                            axp6 = int(exp[5]) * 60
                        except IndexError:
                            axp6 = 0
                        await message.channel.send("5초후에 재획이 시작됩니다.")
                        await asyncio.sleep(5)
                        await message.channel.send("{0.author.mention}재물획득의 비약을 시작중~!!".format(message))
                        await message.channel.send("경험치 쿠폰 {}분 시작되었어~ㅎ".format(exp[0]),delete_after=5)
                        await asyncio.sleep(axp1)
                        if axp2 != 0:
                            await message.channel.send("{0.author.mention}아 경험치 쿠폰을 곧 먹어야해".format(message),delete_after=5)
                            await asyncio.sleep(5)
                            await asyncio.sleep(axp2)
                        if axp3 != 0:
                            await message.channel.send("{0.author.mention}아 경험치 쿠폰을 곧 먹어야해".format(message),delete_after=5)
                            await asyncio.sleep(5)
                            await asyncio.sleep(axp3)
                        if axp4 != 0:
                            await message.channel.send("{0.author.mention}아 경험치 쿠폰을 곧 먹어야해".format(message),delete_after=5)
                            await asyncio.sleep(5)
                            await asyncio.sleep(axp4)
                        if axp5 != 0:
                            await message.channel.send("{0.author.mention}아 경험치 쿠폰을 곧 먹어야해".format(message),delete_after=5)
                            await asyncio.sleep(5)
                            await asyncio.sleep(axp5)
                        if axp6 != 0:
                            await client.send_message(message.channel,"{0.author.mention}아 경험치 폰을 곧 먹어야해".format(message),delete_after=5)
                            await asyncio.sleep(5)
                            await asyncio.sleep(axp6)
                        await message.channel.send("수고했어~",delete_after=5)
            if message.content.startswith("도와줘") or message.content.startswith("help"):
                channel = message.channel
                embed = discord.Embed(
                    title="내가 할 수 있는 일들의 목록이야!",
                    description="""잘 읽고 나한테 말해줘!! ------------------------------------------------------------""",
                    colour=discord.Colour.blue()
                )

                embed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/405331598922219521/608627874299248661/151551155151511515.jpg')

                embed.add_field(name='!융', value='!융 [질문] 종은 것 싫은것을 답해줍니다', inline=False)
                embed.add_field(name='주사위', value='1~6의 숫자를 골라줍니다', inline=False)
                embed.add_field(name='골라', value='골라 [고를꺼1] [고를꺼2] [고를꺼3] ...', inline=False)
                embed.add_field(name='청소', value='메세지를 삭제해줍니다. | 청소 (개수)', inline=False)
                embed.add_field(name='타이머', value='타이머 기능을 작동시킵니다 | 타이머 (초)', inline=False)
                embed.add_field(name='날씨', value='현재와 내일 오전,오후날씨를 알 수 있습니다. | 날씨 (지역)', inline=False)
                embed.add_field(name='운세', value='당신의 오늘의 운을 말해줍니다.', inline=False)       
                embed.add_field(name='이미지검색', value='네이버이미지검색 첫번째 이미지를 가져옵니다 | 이미지검색 (검색어)', inline=False)
                embed.add_field(name='조용', value='메이플안하는사람을 조용히 시킵니다 | 조용 (맨션)', inline=False)
                embed.add_field(name='출근', value='융이 출근하여 다시 말을 할 수 있습니다', inline=False)
                embed.add_field(name='퇴근', value='융이 퇴근하여 사내가 조용합니다.', inline=False)
                await message.channel.send(embed=embed)

                                       

acess_token = os.environ["bot_token"]
client.run(acess_token)
