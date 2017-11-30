# coding: utf-8
# 감성 분석 
# Github에서 다운받아 테스트: https://github.com/hanzhichao2000/pysentiment
# 
# Text 문장을 입력하고, 문장의 감성분석(sentiment analysis)을 수행해 준다.  
# "CNN for Short-Term Stocks Prediction using Tensorflow" blog를 보면
# news 사이트 글의 감성 분석과 stock 가격 정보를 학습하여 미래 가격을 예측. 
# 구현 코드에서 pysentiment를 사용하고 있어, 이를 테스트 함. 
# 
# 2017년 11월 20일  
# coded by funMV  

from pysentiment.hiv4 import HIV4
from pysentiment.lm import LM


text = '''Lately, the Indonesian government has unleashed an array of policies that are keeping mining and oil executives awake at night across this vast and geologically rich archipelago. The unpopular new regulations, aimed at reforming the mining and oil industries, are promoted in the name of "national interest." Yet left uncorrected, they will inevitably lead to a dramatic decline of output in Indonesia's extractive industries, damaging foreign investment and economic growth.
    Particularly hard-hit will be some of Indonesia's less-developed regions such as Kalimantan and Papua, where oil and mining play major economic roles.
    "Equating the government to the Emperor Nero and the local mining industry to ancient Rome," said Bill Sullivan, leading legal consultant for the mining industry in Indonesia, "It is as if Nero is choosing to complacently fiddle while Rome burns."
    Why exactly this fiddling persists—especially since large investors have already cut back from planned capital outlays—is open to debate. Some industry players blame the lack of policy coordination between the central, provincial and local governments. Others blame senior policy makers who meddle with little understanding of the extractive industries.
    Enlarge Image
    image
    image
    Bloomberg News
    Privately, though, both Indonesian and foreign executives claim that the "national interest" is little more than a disguise for rent-seeking, most of the time directed toward corporations with the deepest pockets. Thus the likes of Newmont, BP, Total Oil, and Freeport McMoRan are facing growing concerns from their shareholders and board members. Given the new policies, they wonder whether it's worth the headache to conduct business in Indonesia.
    To be fair, corrupt practices in the name of the greater good have existed long before the current administration. Indonesia has had way too many cooks in the regulatory kitchen ever since former President B.J. Habibie unveiled in 1999 his "Big Bang" policy, which gave unprecedented levels of power to local governors, mayors and local legislators under the flag of regional autonomy. With little national oversight, rent-seeking has run rampant.
    The maze of bureaucracy and overlapping mandates at the local and national levels causes confusion and costly delays for miners and oilmen. But it creates opportunities for those seeking to profit from approval timing or technical issues "Licenses approved by one level of government can easily be denied or rescinded by another," says one senior geologist. "The degrees of freedom for a dispute are enormous, and for a foreign investor, there is little if any legal recourse."
    One mining executive recalls an incident when he requested a letter from the local governor to receive final approvals on a production license. It turned into a classic stick-up, with the governor demanding a sum of $5 million for his signature. Refusal to pay led to the project's standstill.
    Local politicians are not the only ones springing nasty surprises on mining executives. The national government changed mining laws and effectively halted new exploration activities and greenfield projects. Aggressive divestment requirements for foreign investors, high export taxes for unprocessed minerals and mandating mining companies to invest in commercially unsound smelters have caused a furor.
    Hence, there was little surprise when The Fraser Institute's annual survey on mining investment rated Indonesia as the least attractive destination on earth. That places it behind such perennial pariahs as Zimbabwe and the Democratic Republic of the Congo.
    The Indonesian oil and gas industry faces parallel challenges. Most recently, the Indonesian government decided to revoke tax benefits for British and Dutch oil and gas corporations, issuing new tax assessments on a retroactive basis going as far back as a decade. At least one oil major now faces a multi-million dollar tax bill that it must pay or face the prospect of being shut down. "We wouldn't mind [so much] if they decided to change the tax regime going forward," says one senior executive, "but to apply this on a retroactive basis is absolutely ridiculous."
    Adding insult to injury, government officials have also decided to tax exploration activities. One large foreign oil and gas company has already been presented with a tax invoice for its offshore seismic surveys this year. For an industry that needs to be rewarded for taking on exploratory risk, the government has proven itself again to be an unreliable partner.
    With signs now emerging that key government figures have begun to act in harmony to restore investor faith in Indonesia's vulnerable economy, the necessary steps to take are clear: Local governments meddling in the extractive industries need to be given less power over the fate of investors. The process for obtaining licenses and permits should be made simpler, preferably under a single government agency such as the national investment coordinating body. Exploration activities should be rewarded, or at least not penalized.
    And finally, corruption in these industries needs to be more severely policed and punished. While rent-seekers wave the nationalist flag as cover, Indonesia's real national interests, such as energy development and security, are imperiled.
    Of course, identifying the solutions is easier than implementing them. If the national government attempts to strip power from local governments, there is bound to be resistance. As Indonesia heads toward the 2014 elections and fundraising becomes an issue, candidates will stridently oppose reforms that would reduce future rents.
    Even if the government succeeds in reforming local policies, convincing investors could still prove an uphill battle. Daniel Poller, an international mining consultant, observes "natural resource companies think in decades, not years. They have to be able to trust the Indonesian government will not willy-nilly, once again, change the laws to suit their own purposes. Winning back that trust is not as simple as flipping a switch." That means the road to a better Rome will be a long one. But it certainly beats the alternative, which is just more fiddling.'''

# 2개의 모델이 있는데, 첫번쨰로 Harvard IV-4 모델
hiv4 = HIV4()
tokens = hiv4.tokenize(text)
hiv4.get_score(tokens)

# {'Negative': 72,
#  'Polarity': -0.014084506943066852, # -1~+1의 값=(70-72)/(70+72)
#  'Positive': 70,
#  'Subjectivity': 0.30406852183282973} # 주관적인지 객관적인지. 
# 
# 입력 text가 주관적 문장이라면 극성을 분석하여 긍적적인지 부정적인지를 체크한다. 
# 극성 데이터는 0에 가까울 경우는 한쪽으로 치우침이 없음을 보여준다. +1이나 -1로 치우치면 극성이 크다.
# +1: 긍정 측면이 강한 글, -1: 부정 측면이 강한 글 - 이 된다. 

# Loughran and McDonald 모델 
lm = LM()
tokens = lm.tokenize(text)
lm.get_score(tokens)        

# {'Negative': 36,
#  'Polarity': -0.3846153772189351, #(16-36)/52
#  'Positive': 16,
#  'Subjectivity': 0.11134903616413483}


