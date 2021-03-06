from flask import render_template
from modzy import ApiClient

from app import app

client = ApiClient(
    base_url=app.config['API_URL'], api_key=app.config['API_KEY'])

articles = [
    {
        'title': 'Why Tesla Is Designing Chips to Train Its Self-Driving Tech',
        'date': '05-12-2021',
        'author': 'Vignesh K S',
        'content': 'TESLA MAKES CARS. Now, it’s also the latest company to seek an edge in artificial intelligence by making its own silicon chips. At a promotional event last month, Tesla revealed details of a custom AI chip called D1 for training the machine-learning algorithm behind its Autopilot self-driving system. The event focused on Tesla’s AI work and featured a dancing human posing as a humanoid robot the company intends to build. Tesla is the latest nontraditional chipmaker to design its own silicon. As AI becomes more important and costly to deploy, other companies that are heavily invested in the technology—including Google, Amazon, and Microsoft—also now design their own chips. At the event, Tesla CEO Elon Musk said squeezing more performance out of the computer system used to train the company’s neural network will be key to progress in autonomous driving. “If it takes a couple of days for a model to train versus a couple of hours, it’s a big deal,” he said. Tesla already designs chips that interpret sensor input in its cars, after switching from using Nvidia hardware in 2019. But creating a powerful and complex kind of chip needed to train AI algorithms is a lot more expensive and challenging. “If you believe that the solution to autonomous driving is training a large neural network, then what followed was exactly the kind of vertically integrated strategy you’d need,” says Chris Gerdes, director of the Center for Automotive Research at Stanford, who attended the Tesla event. Many car companies use neural networks to identify objects on the road, but Tesla is relying more heavily on the technology, with a single giant neural network known as a “transformer” receiving input from eight cameras at once. “We are effectively building a synthetic animal from the ground up,” Tesla’s AI chief, Andrej Karpathy, said during the August event. “The car can be thought of as an animal. It moves around autonomously, senses the environment and acts autonomously.” Transformer models have provided big advances in areas such as language understanding in recent years; the gains have come from making the models larger and more data-hungry. Training the largest AI programs requires several million dollars worth of cloud computer power. David Kanter, a chip analyst with Real World Technologies, says Musk is betting that by speeding the training, “then I can make this whole machine—the self-driving program—accelerate ahead of the Cruises and the Waymos of the world,” referring to two of Tesla’s rivals in autonomous driving. Gerdes, of Stanford, says Tesla’s strategy is built around its neural network. Unlike many self-driving car companies, Tesla does not use lidar, a more expensive kind of sensor that can see the world in 3D. It relies instead on interpreting scenes by using the neural network algorithm to parse input from its cameras and radar. This is more computationally demanding because the algorithm has to reconstruct a map of its surroundings from the camera feeds rather than relying on sensors that can capture that picture directly. But Tesla also gathers more training data than other car companies. Each of the more than 1 million Teslas on the road sends back to the company the videofeeds from its eight cameras. Tesla says it employs 1,000 people to label those images—noting cars, trucks, traffic signs, lane markings, and other features—to help train the large transformer. At the August event, Tesla also said it can automatically select which images to prioritize in labeling to make the process more efficient. The market for AI training chips is currently dominated by Nvidia, which started out making chips for gaming. The company pivoted to supplying AI chips when it became clear that its graphics processing units (GPUs) were better suited to running large neural networks than the central processing units (CPUs) at the core of general-purpose computers. In a neat bit of recursion, AI is also driving a diversification of chip designs. Chip design normally requires deep technical expertise and judgment, but machine learning has proven effective for automating elements of the process. Google, Samsung, and others are making chips that were designed, in part, by AI.'
    },
    {
        'title': 'Trump attacks media and Mark Milley in foul-mouthed Mar-a-Lago speech',
        'date': '02-12-2021',
        'author': 'Akhilesh M',
        'content': 'In remarks to diners at his Mar-a-Lago resort in Florida on Saturday night, Donald Trump called the American media “crooked bastards” and Gen Mark Milley, the chairman of the joint chiefs of staff, a “fucking idiot”. The meandering, foul-mouthed speech to Turning Point USA, a group for young conservatives, was streamed by Jack Posobiec, a rightwing blogger and provocateur. The insult to the press recalled barbs while Trump was in power, including calling reporters and editors “fake news” and the “enemy of the people”, attacks many in the media regarded as dangerous, inviting political violence. The country is at a very important, dangerous place,” Trump said, amid familiar lies about his defeat in the 2020 election, which he says was the result of electoral fraud. Trump claimed to have transformed Americans’ views of the press, saying “when I first announced I was running in 2015 they had a 94%-95% approval rating. '
    },
    {
        'title': 'Humans Have Broken a Fundamental Law of the Ocean',
        'date': '02-12-2021',
        'author': 'Himavanth',
        'content': 'ON NOVEMBER 19, 1969, the CSS Hudson slipped through the frigid waters of Halifax Harbour in Nova Scotia and out into the open ocean. The research vessel was embarking on what many of the marine scientists on board thought of as the last great, uncharted oceanic voyage: The first complete circumnavigation of the Americas. The ship was bound for Rio de Janeiro, where it would pick up more scientists before passing through Cape Horn—the southernmost point in the Americas—and then head north through the Pacific to traverse the ice-packed Northern Passage back to Halifax Harbour. Along the way, the Hudson would make frequent stops so its scientists could collect samples and take measurements. One of those scientists, Ray Sheldon, had boarded the Hudson in Valparaíso, Chile. A marine ecologist at Canada’s Bedford Institute of Oceanography, Sheldon was fascinated by the microscopic plankton that seemed to be everywhere in the ocean: How far and wide did these tiny organisms spread? To find out, Sheldon and his colleagues hauled buckets of seawater up to the Hudson’s laboratory and used a plankton-counting machine to total up the size and number of creatures they found. Life in the ocean, they discovered, followed a simple mathematical rule: The abundance of an organism is closely linked to its body size. To put it another way, the smaller the organism, the more of them you find in the ocean. Krill are a billion times smaller than tuna, for example, but they are also a billion times more abundant. What was more surprising was how precisely this rule seemed to play out. When Sheldon and his colleagues organized their plankton samples by orders of magnitude, they found that each size bracket contained exactly the same mass of creatures. In a bucket of seawater, one third of the mass of plankton would be between 1 and 10 micrometers, another third would be between 10 and 100 micrometers, and the final third would be between 100 micrometers and 1 millimeter. Each time they would move up a size group, the number of individuals in that group dropped by a factor of 10. The total mass stayed the same, while the size of the populations changed. Sheldon thought this rule might govern all life in the ocean, from the smallest bacterium to the largest whales. This hunch turned out to be true. The Sheldon spectrum, as it became known, has been observed in plankton, fish, and in freshwater ecosystems, too. (In fact, a Russian zoologist had observed the same pattern in soil three decades before Sheldon, but his discovery went mostly unnoticed). “It kind of suggests that no size is better than any other size,” says Eric Galbraith, a professor of earth and planetary sciences at McGill University in Montreal. “Everybody has the same size cells. And basically, for a cell, it doesn’t really matter what body size you’re in, you just kind of tend to do the same thing.” But now humans seem to have broken this fundamental law of the ocean. In a November paper for the journal Science Advances, Galbraith and his colleagues show that the Sheldon spectrum no longer holds true for larger marine creatures. Thanks to industrial fishing, the total ocean biomass of larger fish and marine mammals is much lower than it should be if the Sheldon spectrum was still in effect. “There was this pattern that all life seems to have been following for reasons that we don’t understand,” says Galbraith. “We have changed that over the last 100 years or even less.” To work out if the Sheldon spectrum still held true, Galbraith and his colleagues brought together data on plankton from satellite images and ocean samples, scientific models that predict the abundance of fish, and marine mammal population estimates from the International Union for Conservation of Nature. In total, the group estimated the global abundance of 12 major groups of marine organisms, from bacteria to mammals. They then compared the state of today’s oceans with an estimate of what they might have been like before 1850, by taking into account the fish and mammals that industrialized fishing and whaling have plucked out of the water. To simplify things, the researchers assumed that the levels of bacteria, plankton, and smaller fish in 1850 were similar to today’s levels. When Galbraith and his colleagues looked at this pre-1850 estimate they could immediately see that the Sheldon spectrum largely held true. The researchers found that in the pre-1850 scenario, biomass was remarkably consistent across size brackets. When they totaled up all the organisms that weighed between 1 and 10 grams, it came to 1 billion metric tons. The same was true for all the organisms weighing between 10 and 100 grams, and between 100 grams and 1 kilogram, and so on. Only at the very extreme ends of the spectrum—the smallest bacteria and the biggest whales—did the measurements start to vary. Comparing these pre-1850 estimates to the modern-day models told a very different story. The models suggest that the biomass of fish larger than 10 grams and all marine mammals has shrunk by more than 2 billion metric tons since 1800. The very largest size classes appear to have experienced a reduction in biomass of nearly 90 percent since 1800. Many of the big fish and mammals that used to populate the ocean simply aren’t there anymore. “The world that I grew up in is gone,” says Kristin Kaschner, a marine ecologist at the University of Freiburg in Germany. Between 1890 and 2001, the population of all whale species declined from more than 2.5 million to under 880,000. While the population of some whale species has rebounded since the global whaling moratorium in 1986, many are still endangered. And while the majority of fish stocks are fished in a way that allows them to maintain or grow their populations, just over 34 percent of them are overexploited, which means we’re removing so many fish from a certain area that their populations cannot recover. Some of the fish stocks being overexploited include Japanese anchovy, Alaska pollock, and South American pilchard. “I think we are moving towards a world where the default is not a natural ecosystem in which everything is as you had it before there was human exploitation and intervention,” says Kaschner. Although the picture isn’t rosy at the moment, looking at the size spectrum of marine organisms could be a helpful indicator of ocean health, says Julia Blanchard, an ecologist at the University of Tasmania in Australia. Blanchard has studied coral reefs and found that when the Sheldon spectrum seems out of whack, it’s a sign that the reef ecosystem is no longer healthy. “If we’re looking at improving that, what we might do is ask what would be a level of fishing that would maintain the size spectrum,” she says. One problem is that fisheries often target what scientists call BOFFFFs: big, old, fat, fecund, female fish. Their large bodies are prized by fishers, but BOFFFFs are a vital source of new baby fish. Take these away and the size spectrum quickly veers out of kilter. One way to manage this is to encourage the fishing industry to target medium-size fish, allowing mature ones to replenish depleted populations. Of course, overfishing isn’t the only challenge that marine populations are facing. A worst-case scenario of 5 degrees Celsius of warming would be too hot for 50 percent of fish species, and even 1.5 degrees of warming would still be too much for 10 percent of fish, according to one study. Overfishing means these populations are starting from a much weaker point than they would otherwise be. Take too many fish out of the ocean and you reduce genetic diversity, weaken food webs, and allow ocean habitats to degrade, all of which makes an individual ecosystem more vulnerable to changes. “What’s important is that as you fish out a system and then it’s warmed, it’s much less resilient to that warming,” says Blanchard. The good news is that fish species can bounce back. “They are extremely resilient,” says Ken Andersen, a marine ecologist at the Technical University of Denmark. In September, the International Union for the Conservation of Nature moved four tuna species further down its list of threatened species after their populations started to recover, thanks to stricter fishing quotas and crackdowns on illegal fishing. “It’s easier to stop overfishing than it is to stop climate change,” says Galbraith. “If we fish less, if we allow ecosystems to recover, we can maintain that.”'
    },
    {
        'title': 'Omicron 6 times more transmissible than Delta, could infect even vaccinated',
        'date': '02-12-2021',
        'author': 'Sandesh P',
        'content': 'HYDERABAD: The newly emerged variant of concern B.1.1.529 (Omicron) may not respond to monoclonal antibody therapy or cocktail treatment, experts fear. Based on preliminary analysis of Omicron infections in South Africa and elsewhere, experts suggest that it has six times higher potential to spread (R value) than the Delta variant that had triggered the second wave in India. It could also evade the immune system. It may also cause vaccine breakthrough infections. The Delta variant, which causes heavy infections and mortality, responds to monoclonal antibody therapy. However, its offspring, the Delta plus, did not respond to this therapy, considered a miracle treatment for Covid-19 in initial stages of infection. After the Delta plus, Omicron is the second variant of concern that may not respond to monoclonal antibody treatment. According to Mercy Rophina, research scholar at IGIB, the new lineage carries a total of 53 variants precisely, including 32 spike protein variants. “Most of the observed variants are found to possess resistance against immunity and other functional implications. Six variants with spike receptor binding domain on G339D, S373P, G496S, Q498R and Y505H are found resistant to monoclonal antibodies (mAbs) including etesevimab, bamlanivimab, casirivimab, imdevimab and their cocktails,” Rophina tweeted. In a series of tweets on the new variant, Scaria, an expert in genome sciences, said at least one case of B.1.1.529 in Israel seems to have received a Covid-19 vaccine booster, suggesting the variant can cause vaccine breakthrough infections. “The disease severity is yet to be known, which is the most important point to consider. While vaccine breakthrough infections per se are not the major concern (Delta also caused vaccine breakthrough infections), transmissibility and clinical outcomes (severity and mortality) are the key points,” he said. Rophina, who is from Scaria’s lab, compiled the structural context of the immune escape mutations in Omicron. Scaria said three mutations in the S1/S2 furin cleavage site possibly suggests better cell entry (and may be transmissibility). He, however, added that properties of single mutations don\'t always add up when they occur in combination. Nevertheless, they give potential directions to explore. “Notwithstanding the potential for bias in sequencing, the B.1.1.529 variant seemingly is becoming dominant(almost 0 to 75 % in 2 weeks) in South Africa. More sequences and data are awaited over the coming days. The B.1.1.529 variants seemed to be spreading rapidly in South Africa, faster than other variants of concern we have seen in the past, ” Scaria said in his tweet.'
    },
    {
        'title': 'Bangalore News Live: Don’t panic, no proposal for lockdown, says CM Bommai',
        'date': '30-11-2021',
        'author': 'Mukunda',
        'content': 'Karnataka on Sunday reported 315 fresh Covid-19 cases and two deaths, taking the caseload to 29,95,600 and the toll to 38,198. Bengaluru Urban acted as major contributor of coronavirus cases in the state with 152 fresh infections. Both the deaths were from the city.'
    }
]


@app.route('/', methods=['GET', 'POST'])
def index():

    for article in articles:
        article['url'] = article['title'].replace(' ', '-')

        summarizedTxt = summarizeText(article['content'])
        sentiment = sentimentanalysis(article['content'])
        sentim = ''

        for sen in sentiment:
            if sen['score'] > 0.8:
                sentim = sen['class']

        topics = textTopic(article['content'])
        top5topics = []
        i = 0
        for topic in topics:
            if i < 5:
                top5topics.append(topic)
                i = i+1

        article['sentiment'] = sentim
        article['summary'] = summarizedTxt
        article['topics'] = top5topics

    return render_template('index.html', articles=articles)


def sentimentanalysis(input_text):
    job = client.jobs.submit_text('ed542963de', '1.0.1', {
                                  'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return (result['results']['job']['results.json']['data']['result']['classPredictions'])


def summarizeText(input_text):
    job = client.jobs.submit_text('rs2qqwbjwb', '0.0.2', {
                                  'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return (result['results']['job']['results.json']['summary'])


def textTopic(input_text):
    job = client.jobs.submit_text('m8z2mwe3pt', '0.0.1', {
                                  'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return (result['results']['job']['results.json'])


@app.route('/<url>')
def showArticle(url):
    showArticle = ''
    for article in articles:
        if article['url'] == url:
            showArticle = article

    return render_template('article.html', article=showArticle)
