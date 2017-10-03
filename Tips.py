from __future__ import print_function
import random


kids_quotes = [

    "School and after school activities like soccer practice and drama\
    club is where you make your friends. Be smart. Keep it that way! \
    Never meet anyone in person that you talk to online.",

    "You don't want strangers all up in your business in real life so\
    don't let them be all up in your business online. Keep personal\
    information like your address, phone number, last name, and school\
    name to yourself.",

    "Think twice about posting pics or videos online. What you think\
    might be a cool or cute selfie may be giving away too much of your\
    identity. Ask your parents for their permission before posting.",

    "Ever said something you wish you could take back? In the real\
    world you can apologize. Online... not so much. Once it's posted\
    online it stays there forever. Think really hard about what you're\
    posting online and how you're treating others. Studies have shown\
    some schools may look at your social media precense when trying\
    to decide on whether or not to offer you admission to their\
    school or scholarships.",

    "Do you want someone posting bad or embarassing things from your\
    account making you look bad? I'm guessing you just said NO! Protect\
    your online precense always, don't give any of your passwords away\
    unless you're giving them to your parents or a guardian.",

    "The person you met online that said they're Harry Styles or\
    Taylor Swift most likely aren't. Use your brain, most people\
    online aren't who they say they are.",

    "So you saw a super cool background or game and you want to\
    download it? Wrongo! Downloading things without your parent's ok\
    could lead to a computer virus which could break your computer\
    altogether. It's totes not worth being without a computer and\
    having your parents upset with you.",

    "Show your parents you're responsible and can handle technology.\
    The same rules for online safety and being a good member of\
    internet society apply to cell phones, tablets, and other devices\
    that are connected to the interwebs.",

    "There's a golden rule ...treat others how you want to be\
    treated... Be kind online. Don't be a bully, you're better\
    than that.",

    "One step you can take to protecting yourself on social media is\
    to make sure your privacy settings are in good health. Reach out\
    to your parents to confirm! Better safe than sorry!",

    "Is someone online creeping you out? Is someone being rude or\
    mean? Do you feel like you're in danger? Loop a parent or trusted\
    adult in so they know what the scoop is and so that they can\
    help you.",

    "Oh em gee an email with a link for free tickets to see my\
    favorite singer! Stop! Things that are too good to be true\
    probably are. Opening an email from someone you don't know and\
    clicking on links you're not familiar with could give a hacker\
    personal information about you and your family without you even\
    typing anything.",

    "People online don't need to know that you're going to the\
    library with your friendlies to study and then to the mall or\
    batting cages afterwards. Keep those details off the internet and\
    in texts and in-person discussions with your real friends and\
    family.",

    "Wow that's a nice jacket! Wow that's a nice looking pair of\
    sneakers! If you're online and see something you want to buy\
    talk to your parents first. The last thing you want to do is buy\
    something without their knowledge and be the reason their identity\
    is hacked or worse!",

    "Chatrooms are a breeding ground for strangers and people who may\
    intend to bring you harm. Consult with your parents before\
    entering any chatroom and get their approval.",

    "Your life is like a puzzle. Think about the pieces you're\
    sharing with the world. You don't always need all the pieces\
    of a puzzle to figure out what the picture at the end is. The same\
    goes for sharing details about your life on the internet.",

    "Show your parents you care about what you're doing online. \
    Talk to them about the cool things you're doing and the websites\
    you're visiting. At the end of the day the responsibility of your\
    online choices will fall on your parents. Being open about what\
    you're up to will gain yourself some major respect points!",

    "Guess what? You're not a doctor! If you're feeling sick ...talk\
    to your parents! Don't self diagnose by searching out your\
    symptoms online. These websites don't account for everything and\
    they certainly don't know your history.",

    "Making a screen name or username for that rad video game you're\
    about to play? Best not to use things like your birthdate or\
    last name as part of it. Don't be lazy, be creative!",

    "If rumors and fights start online there's a footprint on the\
    internet of who was involved and when it all started. Don't risk\
    losing your true friends or getting in trouble. Take the high road\
    and find positive ways to support those who are being teased\
    or harassed.",

    "Are you in a bad mood? Upset or angry? Probably not the best time\
    to be posting things online or messaging people. Take a breather\
    and come back when you're feeling better!",

    "Make the world a better place. Spread good vibes and good things\
    and make your contributions to the online world positive ones.\
    You are after all, the future!"

]

adult_quotes = [
    
    "When making online purchases, if you're asked to provide a bank\
    account number or credit or debit card number for purchase, ensure\
    that the website you're completing the transaction on is secure.\
    If the website starts with https, that's http with an s at the end,\
    it is secure. If it's only http without an s at the end, it is not\
    a secure website and your payment information could be at risk of\
    being compromised.",

    "Place passcodes with lock screens on mobile devices like tablets\
    and cell phones to stop prying eyes from strangers and to protect\
    yourself in case your device is stolen.",

    "Don't self diagnose yourself. If you're feeling sick to the point\
    you're consulting health websites trying to find an answer you\
    should be consulting a doctor. These websites don't account for\
    everything and they do not know your health history.",

    "Beware of scams that may involve your friends and family. If\
    accounts of your friends and family become compromised by hackers\
    they may reach out to you on social media asking for a specific\
    amount of money to help them out of a dire situation. Do your due\
    diligence in tracking down your friends or family outside of their\
    web precense to make sure they're ok and if they weren't the ones\
    that reached out to you... inform them their account has been\
    compromised.",

    "Those photos you're posting while you're on vacation are probably\
    beautiful and amazing but they can send a message to the wrong\
    people that you're not home for an extended period of time.\
    Consider posting those photos after you get home.",

    "So you got tickets to that sold out concert or play? Jet setting\
    to another country? Awesome! Think twice before staging a picture\
    with those tickets though. Crafty people could steal your tickets\
    ahead of time from the information captured in your prized photo.",

    "Don't send sensitive information through email. Email is not\
    encrypted, therefore the contents of email are open to anyone who\
    might intercept it.",

    "Check on some of the online services you are using like banking,\
    email, social media, and retail websites. They might offer an\
    additional layer of security on top of your password that is\
    called two factor authentication.",

    "Try not to have your devices automatically connect to open\
    wireless internet networks. These networks can be easily spoofed\
    and you might not be connecting to the trusted network you think\
    you're connecting to. This may put your online activity in\
    harms way.",

    "Check with your internet service provider before you go out and\
    purchase an anti-virus program. Some internet service providers\
    include an anti-virus subscription as part of your plan at no\
    additional cost to you!",

    "Are you a fan of buying and selling things on Craig's list or\
    Facebook? Ask your local police department if they're a safe trade\
    station or encourage them to be if they're not. Meet inside if\
    possible or be in a camera's line of sight if you need to meet\
    outside in the police department parking lot. This takes some of\
    the dangers out of online transactions that require face to face\
    interactions.",

    "Online dating is becoming an increasingly popular way to meet\
    people outside of your normal day to day life. For the first few\
    dates until trust is established, meet in a public space with\
    people around. Try to steer away from being picked up or dropped\
    off until you're comfortable.",

    "Reputable banks will not email you asking for identifying\
    information like social security numbers and account numbers. If\
    you receive an email like this do not click any links in the body\
    of the email. Call the phone number on an official bank statement\
    or on the back of your credit card or debit card to confirm\
    authenticity. If authentic, these situations are best handled over\
    the phone. Encourage your bank to change their practices\
    if they can and at the very least, change the way they notify\
    you.",

    "Protect your computer and always use an anti-virus program like\
    Kaspersky, Trend Micro, Symantec Endpoint, or AVG to safe guard you\
    from viruses and malware. Set these programs to auto update\
    their anti-virus definitions so you can stay on top of the nearly\
    one million new malware threats that are released every day.",

    "Meeting someone for the first time in person that you met online\
    or haven't met face to face? Let a trusted friend know what your\
    plans are, where you're going, what you're doing, and who you're\
    meeting. Ask them to be your phone a friend if things go south\
    and you need to get out of a bad situation.",

    "Use password vaults like 1Password and LastPass to generate and\
    store your passwords and other sensitive data.",

    "Think twice before you download movies or music illegally. The\
    fine per file is up to $150,000 and the possible jail time you\
    could face is up to 5 years.",

    "Choose an extremely strong password to protect your wi-fi network.\
    The default password for most routers can be found through a\
    simple Google search, not very secure at all!",

    "Don't download problematic programs or files. If you download a\
    bad program or files you open yourself up to the potential for\
    viruses. Virus removal can cost hundreds of dollars and you run\
    the risk of losing your data.",

    "Watch out for phishing attempts. These attempts may come in the\
    form of an illegitmate website posing as a legitimate website or\
    emails that look like they're coming from friends or family or a\
    trusted institution like a bank. In phishing attempts you might be\
    prompted to supply personal information like your birthdate,\
    social security number, address, bank account numbers, or\
    passwords. Reputable websites, companies, and trusted friends and\
    family more than likely wouldn't ask you for this information.",

    "Safeguard your data! Consider backing up data like your cherished\
    photos into the cloud. Physical hard drives can break leaving your\
    data unretrievable. Using a cloud storage solution for your files\
    like Dropbox, Google Drive, Box, or One Drive can reduce the risk\
    of data loss due to hardware failures.",

    "Protect your online activity from marketers and hackers. Most web\
    browsers and social media websites offer enhanced privacy settings.\
    Enable these settings when they're available to protect yourself\
    while browsing and using the internet."
    
    ]

parent_quotes = [

    "Keep the family computer in a high traffic area of your home so\
    your children know you're present.",

    "Let your kids know that you trust them to use the internet\
    responsibly. This opens up an established trust with between you\
    and your child regarding their internet use and can make\
    discussions around internet use easier to have.",

    "Continually have open discussions with your children about their\
    internet use and about internet safety.",

    "Consider implementing parental controls to keep your children safe\
    while using the internet.",

    "Discuss the dangers associated with using internet with your\
    children. Explain why they are dangerous and the outcomes that\
    bad choices can have.",

    "Social media websites have age limits on who can use their\
    websites. You and your children should abide by these age limits,\
    the limits are there for a reason.",

    "Research examples of internet safety contracts or create your own\
    internet safety contract that you and your child both agree on that\
    addresses best internet useage practices.",

    "If your child is old enough to be on social media, ensure that\
    they have privacy controls enabled. If you're unsure of how to do\
    this, social media websites provide great documentation that will\
    walk you through it.",

    "Follow or become friends with your children on social media if\
    they have social media accounts. Regularly review your children's\
    friends and posts and strike up a conversation with your children\
    if you have questions.",

    "Don't allow your children to keep their mobile devices in their\
    room at night. Consider establishing a central charging station\
    in your living room, kitchen, or bedroom where devices go to\
    sleep every night.",

    "iCloud and Google Play passwords should be for your eyes only.\
    Giving your kids these passwords opens up the opportunity for your\
    kids to download any kind of apps and reset their devices without\
    your permission. Resetting a device can wipe out any parental\
    controls you may have on the device. Kids are smart,\
    don't underestimate them.",

    "Be aware of anonymous texting apps like Snapchat, Kik, and\
    Yik Yak. Also, provocative social media websites like Ask.fm.\
    Use of these apps and sites should be prohibited. Consider working\
    this into an internet safety contract.",

    "Monitor your child's device and usage. This is included but not\
    limited to installed apps, browsing history, and text message\
    recipients.",

    "Don't let the amount of internet safety threats we face deter you\
    from letting your children use the internet. When rules are\
    followed to deter threats the internet can be a great resource for\
    education and personal interests.",

    "Encourage your children to tell you immediately if they're having\
    an issue or are feeling uncomfortable about something that happened\
    or that they saw on the internet. Ensure them that they will not\
    have their internet privleges taken away for sharing this\
    information. The goal is not to scare them into hiding a real\
    problem but to promote a safe space for sharing concerns.",

    "Talk to your kids about the importance of not sharing\
    identifying information about themselves online. The accronymn\
    YAPPY can be used. Y for Your full name, A for age, P for phone\
    number, P for passwords, Y for your plans. That's Y-A-P-P-Y - \
    Yappy!",

    "Explore trusted resources like government resources to stay on\
    top of the potential threats your kids can face. These trends will\
    change over time, just like the technology behind it.",

    "Ensure all operating systems are patched as soon as patches are\
    released.",

    "Teach your kids about common sense internet useage such as not\
    meeting anyone they speak to online in person, not downloading\
    software or files without your permission, and not sending or\
    posting pictures without a parent's permission. The internet is a\
    great resource for finding tips for your kids and so is the skill.\
    Simply ask Alexa, give me tips for kids to access the portion of \
    this skill that is directed at adolescents.",

    "Parent's should encourage their kids to be good citizens online.\
    They should be encouraged not to partake in online bullying and to\
    report online bullying whether it is happening to them or to\
    someone else.",

    "Help walk your child through critical thinking in regards to web\
    content. Help show them proper ways of research and teach them the\
    difference between user submitted content, authoritative\
    content, and spam.",

    "Just because you're a fan of YouTube doesn't mean your child\
    should be. At least not of the version of YouTube that you watch.\
    YouTube offers YouTube Kids which is the kid friendly version of\
    YouTube!"

]