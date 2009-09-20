'''
Created on Sep 2, 2009

@author: Penn
'''

import news

def main():
    t = 'A look at the number of viewers (in millions) for some of President Obama\'s nationally televised prime-time appearances. Source: NielsenThe Sunday shows Obama plans to appear on the Sunday morning talk shows of ABC, NBC, CBS and sit for interviews with CNN and Spanish-language network Univision. He\'s skipping Fox, whose news channel he has said is "entirely devoted to attacking my administration." White House spokesman Robert Gibbs says the interviews are "an attempt by the president to speak to as many different people as he can on an issue that\'s as important as something like health care reform or on Afghanistan." Previous presidents have been grilled on the Sunday shows, but not all in one day. Obama drew 3.7 million viewers to CBS\' Face the Nation in March, according to the Nielsen ratings company.Busy week The Late Show with David Letterman stint will be the first by a sitting president on that CBS show, the network says. Obama last chatted with Letterman during the campaign. He\'ll tape the show in New York City on Monday afternoon, at the start of a busy week of diplomacy. He also addresses the United Nations and the global foundation run by Bill Clinton and hosts world leaders in Pittsburgh for the Group of 20 economic summit.Comparing presidents Obama will have done 124 print, broadcast and radio interviews by day\'s end on Sunday, according to a tally by Martha Joynt Kumar, a political scientist at Towson University in Maryland. George W. Bush did 40 and Bill Clinton did 46 by the same point in their presidencies. She says Obama, as a former lawyer and law professor, "likes to talk about things in depth."Too much Obama? Robert Thompson, director of the Bleier Center for Television and Popular Culture at Syracuse University, says the president risks overexposure but has little choice if he wants to get out his message. "The idea that familiarity breeds contempt may be a clich because there\'s some truth to it," he says. Still, Thompson says most Americans won\'t be watching Obama on Sunday or Monday: "The reason he\'s doing these shows is because the audience is fragmented."Interview rhythms There are certain rhythms during Obama\'s TV interviews. He can be a salesman, trying to sell his plans for health care or proposals to cushion the blows of the recession. He can be playful, such as announcing that the First Family would get a dog. He can be candid, as he did in January, telling ABC\'s George Stephanopoulos that the prison for terrorism suspects at Guantanamo Bay, Cuba, would not close within 100 days of his taking office. Obama also can be combative, such as last week when he took exception to CBS reporter Steve Kroft\'s characterization that he "nationalized" auto companies and some banks. Obama pushed back: "Oh, wait. Hold on. Time out a second, Steve. Come on, now."A gutter ball The danger of doing a lot of interviews is the chance of a gaffe. Obama had to apologize for a remark he made in March on NBC\'s Tonight Show, saying his lack of skill at bowling "was like Special Olympics or something." He knew he goofed and apologized to Special Olympics Chairman Timothy Shriver before the show aired. More than 14.6 million people watched the show, according to Nielsen.Meeting the press Obama has held four prime-time news conferences since taking office. He always opens with a statement read from a teleprompter. He also calls on a variety of reporters, including those from the major TV networks, as well as scribes from regional newspapers such as The Plain Dealer in Cleveland, and those more limited in scope, such as Stars and Stripes.'


    news.setName("Test")
    news.setColumns(4)
    news.addArticle(news.convert(t), "Democratize the Means of Production")
    #news.addImagetoArticle(news.convert('adlkfjsd;l\\\"\"\kfasdmielsdkjas;dlkfjsdf'), news.convert("google.jpg"))
    #news.addArticle("I like to move it move it!")
    news.Generate()
    f = open('latex_test.tex', 'w')
    f.write(news.Latex)

if __name__ == "__main__":
    main()
