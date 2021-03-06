# 빈도수 (dict 이용)

lyric = '''이제야 목적지를 정했지만
가려한 날 막아서네
난 갈 길이 먼데
새빨간 얼굴로 화를 냈던
친구가 생각나네
이미 난 발걸음을 떼었지만
가려한 날 재촉하네
걷기도 힘든데
새파랗게 겁에 질려 도망간
친구가 뇌에 맴도네
건반처럼 생긴 도로 위
수많은 동그라미들 모두가
멈췄다 굴렀다 말은 잘 들어
그건 나도 문제가 아냐
붉은색 푸른색
그 사이 3초 그 짧은 시간
노란색 빛을 내는
저기 저 신호등이
내 머릿속을 텅 비워버려
내가 빠른 지도'''

rt = lyric.split()   #리스트

lyric_dict = dict()
for text in rt:
    print (text, end=",")
    if text in lyric_dict:
        lyric_dict[text] = lyric_dict[text] + 1 
    else:
        lyric_dict[text] = 1

lyric_dict