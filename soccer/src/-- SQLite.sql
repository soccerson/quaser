-- SQLite
CREATE TABLE 対戦募集一覧(学校名 TEXT, 場所 TEXT, 大会順位 INTEGER, 勝率 REAL, 失点率 REAL, 得点率 REAL);

INSERT INTO 対戦募集一覧(学校名, 場所, 大会順位, 勝率, 失点率, 得点率)
VALUES    
    ('横浜創英高校', '神奈川県横浜市神奈川区西大口28', 1, 0.85, 0.2, 1.8),
    ('千葉県立柏高校', '千葉県柏市布施254', 2, 0.80, 0.3, 1.7),
    ('前橋育英高校', '群馬県前橋市朝日が丘町13番地', 3, 0.78, 0.25, 1.5),
    ('桐光学園高校', '神奈川県川崎市麻生区栗木3-12-1', 4, 0.75, 0.35, 1.6),
    ('青森山田高校', '青森県青森市青葉3-13-40', 5, 0.72, 0.4, 1.5),
    ('東京都立三鷹高校', '東京都三鷹市新川6-21-21', 6, 0.70, 0.5, 1.4),
    ('流通経済大学付属柏高校', '千葉県柏市十余二1-20', 7, 0.68, 0.45, 1.3),
    ('埼玉栄高校', '埼玉県さいたま市西区西大宮3-11-1', 8, 0.67, 0.55, 1.2),
    ('市立船橋高校', '千葉県船橋市市場4-5-1', 9, 0.65, 0.6, 1.1),
    ('東京学館高校', '千葉県印旛郡酒々井町伊篠21', 10, 0.64, 0.65, 1.0),
    ('國學院久我山高校', '東京都杉並区久我山1-9-1', 11, 0.63, 0.55, 0.9),
    ('東海大菅生高校', '東京都あきる野市菅生1817', 12, 0.62, 0.6, 0.8),
    ('八千代松陰高校', '千葉県八千代市村上727', 13, 0.60, 0.7, 0.85),
    ('武南高校', '埼玉県蕨市塚越5-10-21', 14, 0.58, 0.6, 0.8),
    ('湘南工科大学附属高校', '神奈川県藤沢市辻堂西海岸1-1-25', 15, 0.55, 0.75, 0.9),
    ('東邦大学付属東邦高校', '千葉県習志野市泉町2-1-37', 16, 0.53, 0.65, 0.7),
    ('日本大学鶴ヶ丘高校', '東京都杉並区和泉2-26-12', 17, 0.50, 0.7, 0.6),
    ('川崎市立橘高校', '神奈川県川崎市中原区中丸子562', 18, 0.48, 0.8, 0.5),
    ('茗溪学園高校', '茨城県つくば市稲荷前1-1', 19, 0.45, 0.85, 0.4),
    ('専修大学附属高校', '東京都杉並区和泉4-4-1', 20, 0.42, 0.9, 0.3);