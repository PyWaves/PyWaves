import math
import pywaves
import axolotl_curve25519 as curve
import os
import pywaves.crypto as crypto
import time
import struct
import json
import base58
import base64
import logging
import requests

wordList = ['abandon', 'ability', 'able', 'about', 'above', 'absent', 'absorb', 'abstract', 'absurd', 'abuse', 'access',
            'accident', 'account', 'accuse', 'achieve', 'acid', 'acoustic', 'acquire', 'across', 'act', 'action',
            'actor', 'actress', 'actual', 'adapt', 'add', 'addict', 'address', 'adjust', 'admit', 'adult', 'advance',
            'advice', 'aerobic', 'affair', 'afford', 'afraid', 'again', 'age', 'agent', 'agree', 'ahead', 'aim', 'air',
            'airport', 'aisle', 'alarm', 'album', 'alcohol', 'alert', 'alien', 'all', 'alley', 'allow', 'almost',
            'alone', 'alpha', 'already', 'also', 'alter', 'always', 'amateur', 'amazing', 'among', 'amount', 'amused',
            'analyst', 'anchor', 'ancient', 'anger', 'angle', 'angry', 'animal', 'ankle', 'announce', 'annual',
            'another', 'answer', 'antenna', 'antique', 'anxiety', 'any', 'apart', 'apology', 'appear', 'apple',
            'approve', 'april', 'arch', 'arctic', 'area', 'arena', 'argue', 'arm', 'armed', 'armor', 'army', 'around',
            'arrange', 'arrest', 'arrive', 'arrow', 'art', 'artefact', 'artist', 'artwork', 'ask', 'aspect', 'assault',
            'asset', 'assist', 'assume', 'asthma', 'athlete', 'atom', 'attack', 'attend', 'attitude', 'attract',
            'auction', 'audit', 'august', 'aunt', 'author', 'auto', 'autumn', 'average', 'avocado', 'avoid', 'awake',
            'aware', 'away', 'awesome', 'awful', 'awkward', 'axis', 'baby', 'bachelor', 'bacon', 'badge', 'bag',
            'balance', 'balcony', 'ball', 'bamboo', 'banana', 'banner', 'bar', 'barely', 'bargain', 'barrel', 'base',
            'basic', 'basket', 'battle', 'beach', 'bean', 'beauty', 'because', 'become', 'beef', 'before', 'begin',
            'behave', 'behind', 'believe', 'below', 'belt', 'bench', 'benefit', 'best', 'betray', 'better', 'between',
            'beyond', 'bicycle', 'bid', 'bike', 'bind', 'biology', 'bird', 'birth', 'bitter', 'black', 'blade', 'blame',
            'blanket', 'blast', 'bleak', 'bless', 'blind', 'blood', 'blossom', 'blouse', 'blue', 'blur', 'blush',
            'board', 'boat', 'body', 'boil', 'bomb', 'bone', 'bonus', 'book', 'boost', 'border', 'boring', 'borrow',
            'boss', 'bottom', 'bounce', 'box', 'boy', 'bracket', 'brain', 'brand', 'brass', 'brave', 'bread', 'breeze',
            'brick', 'bridge', 'brief', 'bright', 'bring', 'brisk', 'broccoli', 'broken', 'bronze', 'broom', 'brother',
            'brown', 'brush', 'bubble', 'buddy', 'budget', 'buffalo', 'build', 'bulb', 'bulk', 'bullet', 'bundle',
            'bunker', 'burden', 'burger', 'burst', 'bus', 'business', 'busy', 'butter', 'buyer', 'buzz', 'cabbage',
            'cabin', 'cable', 'cactus', 'cage', 'cake', 'call', 'calm', 'camera', 'camp', 'can', 'canal', 'cancel',
            'candy', 'cannon', 'canoe', 'canvas', 'canyon', 'capable', 'capital', 'captain', 'car', 'carbon', 'card',
            'cargo', 'carpet', 'carry', 'cart', 'case', 'cash', 'casino', 'castle', 'casual', 'cat', 'catalog', 'catch',
            'category', 'cattle', 'caught', 'cause', 'caution', 'cave', 'ceiling', 'celery', 'cement', 'census',
            'century', 'cereal', 'certain', 'chair', 'chalk', 'champion', 'change', 'chaos', 'chapter', 'charge',
            'chase', 'chat', 'cheap', 'check', 'cheese', 'chef', 'cherry', 'chest', 'chicken', 'chief', 'child',
            'chimney', 'choice', 'choose', 'chronic', 'chuckle', 'chunk', 'churn', 'cigar', 'cinnamon', 'circle',
            'citizen', 'city', 'civil', 'claim', 'clap', 'clarify', 'claw', 'clay', 'clean', 'clerk', 'clever', 'click',
            'client', 'cliff', 'climb', 'clinic', 'clip', 'clock', 'clog', 'close', 'cloth', 'cloud', 'clown', 'club',
            'clump', 'cluster', 'clutch', 'coach', 'coast', 'coconut', 'code', 'coffee', 'coil', 'coin', 'collect',
            'color', 'column', 'combine', 'come', 'comfort', 'comic', 'common', 'company', 'concert', 'conduct',
            'confirm', 'congress', 'connect', 'consider', 'control', 'convince', 'cook', 'cool', 'copper', 'copy',
            'coral', 'core', 'corn', 'correct', 'cost', 'cotton', 'couch', 'country', 'couple', 'course', 'cousin',
            'cover', 'coyote', 'crack', 'cradle', 'craft', 'cram', 'crane', 'crash', 'crater', 'crawl', 'crazy',
            'cream', 'credit', 'creek', 'crew', 'cricket', 'crime', 'crisp', 'critic', 'crop', 'cross', 'crouch',
            'crowd', 'crucial', 'cruel', 'cruise', 'crumble', 'crunch', 'crush', 'cry', 'crystal', 'cube', 'culture',
            'cup', 'cupboard', 'curious', 'current', 'curtain', 'curve', 'cushion', 'custom', 'cute', 'cycle', 'dad',
            'damage', 'damp', 'dance', 'danger', 'daring', 'dash', 'daughter', 'dawn', 'day', 'deal', 'debate',
            'debris', 'decade', 'december', 'decide', 'decline', 'decorate', 'decrease', 'deer', 'defense', 'define',
            'defy', 'degree', 'delay', 'deliver', 'demand', 'demise', 'denial', 'dentist', 'deny', 'depart', 'depend',
            'deposit', 'depth', 'deputy', 'derive', 'describe', 'desert', 'design', 'desk', 'despair', 'destroy',
            'detail', 'detect', 'develop', 'device', 'devote', 'diagram', 'dial', 'diamond', 'diary', 'dice', 'diesel',
            'diet', 'differ', 'digital', 'dignity', 'dilemma', 'dinner', 'dinosaur', 'direct', 'dirt', 'disagree',
            'discover', 'disease', 'dish', 'dismiss', 'disorder', 'display', 'distance', 'divert', 'divide', 'divorce',
            'dizzy', 'doctor', 'document', 'dog', 'doll', 'dolphin', 'domain', 'donate', 'donkey', 'donor', 'door',
            'dose', 'double', 'dove', 'draft', 'dragon', 'drama', 'drastic', 'draw', 'dream', 'dress', 'drift', 'drill',
            'drink', 'drip', 'drive', 'drop', 'drum', 'dry', 'duck', 'dumb', 'dune', 'during', 'dust', 'dutch', 'duty',
            'dwarf', 'dynamic', 'eager', 'eagle', 'early', 'earn', 'earth', 'easily', 'east', 'easy', 'echo', 'ecology',
            'economy', 'edge', 'edit', 'educate', 'effort', 'egg', 'eight', 'either', 'elbow', 'elder', 'electric',
            'elegant', 'element', 'elephant', 'elevator', 'elite', 'else', 'embark', 'embody', 'embrace', 'emerge',
            'emotion', 'employ', 'empower', 'empty', 'enable', 'enact', 'end', 'endless', 'endorse', 'enemy', 'energy',
            'enforce', 'engage', 'engine', 'enhance', 'enjoy', 'enlist', 'enough', 'enrich', 'enroll', 'ensure',
            'enter', 'entire', 'entry', 'envelope', 'episode', 'equal', 'equip', 'era', 'erase', 'erode', 'erosion',
            'error', 'erupt', 'escape', 'essay', 'essence', 'estate', 'eternal', 'ethics', 'evidence', 'evil', 'evoke',
            'evolve', 'exact', 'example', 'excess', 'exchange', 'excite', 'exclude', 'excuse', 'execute', 'exercise',
            'exhaust', 'exhibit', 'exile', 'exist', 'exit', 'exotic', 'expand', 'expect', 'expire', 'explain', 'expose',
            'express', 'extend', 'extra', 'eye', 'eyebrow', 'fabric', 'face', 'faculty', 'fade', 'faint', 'faith',
            'fall', 'false', 'fame', 'family', 'famous', 'fan', 'fancy', 'fantasy', 'farm', 'fashion', 'fat', 'fatal',
            'father', 'fatigue', 'fault', 'favorite', 'feature', 'february', 'federal', 'fee', 'feed', 'feel', 'female',
            'fence', 'festival', 'fetch', 'fever', 'few', 'fiber', 'fiction', 'field', 'figure', 'file', 'film',
            'filter', 'final', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fiscal', 'fish', 'fit',
            'fitness', 'fix', 'flag', 'flame', 'flash', 'flat', 'flavor', 'flee', 'flight', 'flip', 'float', 'flock',
            'floor', 'flower', 'fluid', 'flush', 'fly', 'foam', 'focus', 'fog', 'foil', 'fold', 'follow', 'food',
            'foot', 'force', 'forest', 'forget', 'fork', 'fortune', 'forum', 'forward', 'fossil', 'foster', 'found',
            'fox', 'fragile', 'frame', 'frequent', 'fresh', 'friend', 'fringe', 'frog', 'front', 'frost', 'frown',
            'frozen', 'fruit', 'fuel', 'fun', 'funny', 'furnace', 'fury', 'future', 'gadget', 'gain', 'galaxy',
            'gallery', 'game', 'gap', 'garage', 'garbage', 'garden', 'garlic', 'garment', 'gas', 'gasp', 'gate',
            'gather', 'gauge', 'gaze', 'general', 'genius', 'genre', 'gentle', 'genuine', 'gesture', 'ghost', 'giant',
            'gift', 'giggle', 'ginger', 'giraffe', 'girl', 'give', 'glad', 'glance', 'glare', 'glass', 'glide',
            'glimpse', 'globe', 'gloom', 'glory', 'glove', 'glow', 'glue', 'goat', 'goddess', 'gold', 'good', 'goose',
            'gorilla', 'gospel', 'gossip', 'govern', 'gown', 'grab', 'grace', 'grain', 'grant', 'grape', 'grass',
            'gravity', 'great', 'green', 'grid', 'grief', 'grit', 'grocery', 'group', 'grow', 'grunt', 'guard', 'guess',
            'guide', 'guilt', 'guitar', 'gun', 'gym', 'habit', 'hair', 'half', 'hammer', 'hamster', 'hand', 'happy',
            'harbor', 'hard', 'harsh', 'harvest', 'hat', 'have', 'hawk', 'hazard', 'head', 'health', 'heart', 'heavy',
            'hedgehog', 'height', 'hello', 'helmet', 'help', 'hen', 'hero', 'hidden', 'high', 'hill', 'hint', 'hip',
            'hire', 'history', 'hobby', 'hockey', 'hold', 'hole', 'holiday', 'hollow', 'home', 'honey', 'hood', 'hope',
            'horn', 'horror', 'horse', 'hospital', 'host', 'hotel', 'hour', 'hover', 'hub', 'huge', 'human', 'humble',
            'humor', 'hundred', 'hungry', 'hunt', 'hurdle', 'hurry', 'hurt', 'husband', 'hybrid', 'ice', 'icon', 'idea',
            'identify', 'idle', 'ignore', 'ill', 'illegal', 'illness', 'image', 'imitate', 'immense', 'immune',
            'impact', 'impose', 'improve', 'impulse', 'inch', 'include', 'income', 'increase', 'index', 'indicate',
            'indoor', 'industry', 'infant', 'inflict', 'inform', 'inhale', 'inherit', 'initial', 'inject', 'injury',
            'inmate', 'inner', 'innocent', 'input', 'inquiry', 'insane', 'insect', 'inside', 'inspire', 'install',
            'intact', 'interest', 'into', 'invest', 'invite', 'involve', 'iron', 'island', 'isolate', 'issue', 'item',
            'ivory', 'jacket', 'jaguar', 'jar', 'jazz', 'jealous', 'jeans', 'jelly', 'jewel', 'job', 'join', 'joke',
            'journey', 'joy', 'judge', 'juice', 'jump', 'jungle', 'junior', 'junk', 'just', 'kangaroo', 'keen', 'keep',
            'ketchup', 'key', 'kick', 'kid', 'kidney', 'kind', 'kingdom', 'kiss', 'kit', 'kitchen', 'kite', 'kitten',
            'kiwi', 'knee', 'knife', 'knock', 'know', 'lab', 'label', 'labor', 'ladder', 'lady', 'lake', 'lamp',
            'language', 'laptop', 'large', 'later', 'latin', 'laugh', 'laundry', 'lava', 'law', 'lawn', 'lawsuit',
            'layer', 'lazy', 'leader', 'leaf', 'learn', 'leave', 'lecture', 'left', 'leg', 'legal', 'legend', 'leisure',
            'lemon', 'lend', 'length', 'lens', 'leopard', 'lesson', 'letter', 'level', 'liar', 'liberty', 'library',
            'license', 'life', 'lift', 'light', 'like', 'limb', 'limit', 'link', 'lion', 'liquid', 'list', 'little',
            'live', 'lizard', 'load', 'loan', 'lobster', 'local', 'lock', 'logic', 'lonely', 'long', 'loop', 'lottery',
            'loud', 'lounge', 'love', 'loyal', 'lucky', 'luggage', 'lumber', 'lunar', 'lunch', 'luxury', 'lyrics',
            'machine', 'mad', 'magic', 'magnet', 'maid', 'mail', 'main', 'major', 'make', 'mammal', 'man', 'manage',
            'mandate', 'mango', 'mansion', 'manual', 'maple', 'marble', 'march', 'margin', 'marine', 'market',
            'marriage', 'mask', 'mass', 'master', 'match', 'material', 'math', 'matrix', 'matter', 'maximum', 'maze',
            'meadow', 'mean', 'measure', 'meat', 'mechanic', 'medal', 'media', 'melody', 'melt', 'member', 'memory',
            'mention', 'menu', 'mercy', 'merge', 'merit', 'merry', 'mesh', 'message', 'metal', 'method', 'middle',
            'midnight', 'milk', 'million', 'mimic', 'mind', 'minimum', 'minor', 'minute', 'miracle', 'mirror', 'misery',
            'miss', 'mistake', 'mix', 'mixed', 'mixture', 'mobile', 'model', 'modify', 'mom', 'moment', 'monitor',
            'monkey', 'monster', 'month', 'moon', 'moral', 'more', 'morning', 'mosquito', 'mother', 'motion', 'motor',
            'mountain', 'mouse', 'move', 'movie', 'much', 'muffin', 'mule', 'multiply', 'muscle', 'museum', 'mushroom',
            'music', 'must', 'mutual', 'myself', 'mystery', 'myth', 'naive', 'name', 'napkin', 'narrow', 'nasty',
            'nation', 'nature', 'near', 'neck', 'need', 'negative', 'neglect', 'neither', 'nephew', 'nerve', 'nest',
            'net', 'network', 'neutral', 'never', 'news', 'next', 'nice', 'night', 'noble', 'noise', 'nominee',
            'noodle', 'normal', 'north', 'nose', 'notable', 'note', 'nothing', 'notice', 'novel', 'now', 'nuclear',
            'number', 'nurse', 'nut', 'oak', 'obey', 'object', 'oblige', 'obscure', 'observe', 'obtain', 'obvious',
            'occur', 'ocean', 'october', 'odor', 'off', 'offer', 'office', 'often', 'oil', 'okay', 'old', 'olive',
            'olympic', 'omit', 'once', 'one', 'onion', 'online', 'only', 'open', 'opera', 'opinion', 'oppose',
            'option', 'orange', 'orbit', 'orchard', 'order', 'ordinary', 'organ', 'orient', 'original', 'orphan',
            'ostrich', 'other', 'outdoor', 'outer', 'output', 'outside', 'oval', 'oven', 'over', 'own', 'owner',
            'oxygen', 'oyster', 'ozone', 'pact', 'paddle', 'page', 'pair', 'palace', 'palm', 'panda', 'panel', 'panic',
            'panther', 'paper', 'parade', 'parent', 'park', 'parrot', 'party', 'pass', 'patch', 'path', 'patient',
            'patrol', 'pattern', 'pause', 'pave', 'payment', 'peace', 'peanut', 'pear', 'peasant', 'pelican', 'pen',
            'penalty', 'pencil', 'people', 'pepper', 'perfect', 'permit', 'person', 'pet', 'phone', 'photo', 'phrase',
            'physical', 'piano', 'picnic', 'picture', 'piece', 'pig', 'pigeon', 'pill', 'pilot', 'pink', 'pioneer',
            'pipe', 'pistol', 'pitch', 'pizza', 'place', 'planet', 'plastic', 'plate', 'play', 'please', 'pledge',
            'pluck', 'plug', 'plunge', 'poem', 'poet', 'point', 'polar', 'pole', 'police', 'pond', 'pony', 'pool',
            'popular', 'portion', 'position', 'possible', 'post', 'potato', 'pottery', 'poverty', 'powder', 'power',
            'practice', 'praise', 'predict', 'prefer', 'prepare', 'present', 'pretty', 'prevent', 'price', 'pride',
            'primary', 'print', 'priority', 'prison', 'private', 'prize', 'problem', 'process', 'produce', 'profit',
            'program', 'project', 'promote', 'proof', 'property', 'prosper', 'protect', 'proud', 'provide', 'public',
            'pudding', 'pull', 'pulp', 'pulse', 'pumpkin', 'punch', 'pupil', 'puppy', 'purchase', 'purity', 'purpose',
            'purse', 'push', 'put', 'puzzle', 'pyramid', 'quality', 'quantum', 'quarter', 'question', 'quick', 'quit',
            'quiz', 'quote', 'rabbit', 'raccoon', 'race', 'rack', 'radar', 'radio', 'rail', 'rain', 'raise', 'rally',
            'ramp', 'ranch', 'random', 'range', 'rapid', 'rare', 'rate', 'rather', 'raven', 'raw', 'razor', 'ready',
            'real', 'reason', 'rebel', 'rebuild', 'recall', 'receive', 'recipe', 'record', 'recycle', 'reduce',
            'reflect', 'reform', 'refuse', 'region', 'regret', 'regular', 'reject', 'relax', 'release', 'relief',
            'rely', 'remain', 'remember', 'remind', 'remove', 'render', 'renew', 'rent', 'reopen', 'repair', 'repeat',
            'replace', 'report', 'require', 'rescue', 'resemble', 'resist', 'resource', 'response', 'result', 'retire',
            'retreat', 'return', 'reunion', 'reveal', 'review', 'reward', 'rhythm', 'rib', 'ribbon', 'rice', 'rich',
            'ride', 'ridge', 'rifle', 'right', 'rigid', 'ring', 'riot', 'ripple', 'risk', 'ritual', 'rival', 'river',
            'road', 'roast', 'robot', 'robust', 'rocket', 'romance', 'roof', 'rookie', 'room', 'rose', 'rotate',
            'rough', 'round', 'route', 'royal', 'rubber', 'rude', 'rug', 'rule', 'run', 'runway', 'rural', 'sad',
            'saddle', 'sadness', 'safe', 'sail', 'salad', 'salmon', 'salon', 'salt', 'salute', 'same', 'sample', 'sand',
            'satisfy', 'satoshi', 'sauce', 'sausage', 'save', 'say', 'scale', 'scan', 'scare', 'scatter', 'scene',
            'scheme', 'school', 'science', 'scissors', 'scorpion', 'scout', 'scrap', 'screen', 'script', 'scrub', 'sea',
            'search', 'season', 'seat', 'second', 'secret', 'section', 'security', 'seed', 'seek', 'segment', 'select',
            'sell', 'seminar', 'senior', 'sense', 'sentence', 'series', 'service', 'session', 'settle', 'setup',
            'seven', 'shadow', 'shaft', 'shallow', 'share', 'shed', 'shell', 'sheriff', 'shield', 'shift', 'shine',
            'ship', 'shiver', 'shock', 'shoe', 'shoot', 'shop', 'short', 'shoulder', 'shove', 'shrimp', 'shrug',
            'shuffle', 'shy', 'sibling', 'sick', 'side', 'siege', 'sight', 'sign', 'silent', 'silk', 'silly', 'silver',
            'similar', 'simple', 'since', 'sing', 'siren', 'sister', 'situate', 'six', 'size', 'skate', 'sketch', 'ski',
            'skill', 'skin', 'skirt', 'skull', 'slab', 'slam', 'sleep', 'slender', 'slice', 'slide', 'slight', 'slim',
            'slogan', 'slot', 'slow', 'slush', 'small', 'smart', 'smile', 'smoke', 'smooth', 'snack', 'snake', 'snap',
            'sniff', 'snow', 'soap', 'soccer', 'social', 'sock', 'soda', 'soft', 'solar', 'soldier', 'solid',
            'solution', 'solve', 'someone', 'song', 'soon', 'sorry', 'sort', 'soul', 'sound', 'soup', 'source', 'south',
            'space', 'spare', 'spatial', 'spawn', 'speak', 'special', 'speed', 'spell', 'spend', 'sphere', 'spice',
            'spider', 'spike', 'spin', 'spirit', 'split', 'spoil', 'sponsor', 'spoon', 'sport', 'spot', 'spray',
            'spread', 'spring', 'spy', 'square', 'squeeze', 'squirrel', 'stable', 'stadium', 'staff', 'stage', 'stairs',
            'stamp', 'stand', 'start', 'state', 'stay', 'steak', 'steel', 'stem', 'step', 'stereo', 'stick', 'still',
            'sting', 'stock', 'stomach', 'stone', 'stool', 'story', 'stove', 'strategy', 'street', 'strike', 'strong',
            'struggle', 'student', 'stuff', 'stumble', 'style', 'subject', 'submit', 'subway', 'success', 'such',
            'sudden', 'suffer', 'sugar', 'suggest', 'suit', 'summer', 'sun', 'sunny', 'sunset', 'super', 'supply',
            'supreme', 'sure', 'surface', 'surge', 'surprise', 'surround', 'survey', 'suspect', 'sustain', 'swallow',
            'swamp', 'swap', 'swarm', 'swear', 'sweet', 'swift', 'swim', 'swing', 'switch', 'sword', 'symbol',
            'symptom', 'syrup', 'system', 'table', 'tackle', 'tag', 'tail', 'talent', 'talk', 'tank', 'tape', 'target',
            'task', 'taste', 'tattoo', 'taxi', 'teach', 'team', 'tell', 'ten', 'tenant', 'tennis', 'tent', 'term',
            'test', 'text', 'thank', 'that', 'theme', 'then', 'theory', 'there', 'they', 'thing', 'this', 'thought',
            'three', 'thrive', 'throw', 'thumb', 'thunder', 'ticket', 'tide', 'tiger', 'tilt', 'timber', 'time', 'tiny',
            'tip', 'tired', 'tissue', 'title', 'toast', 'tobacco', 'today', 'toddler', 'toe', 'together', 'toilet',
            'token', 'tomato', 'tomorrow', 'tone', 'tongue', 'tonight', 'tool', 'tooth', 'top', 'topic', 'topple',
            'torch', 'tornado', 'tortoise', 'toss', 'total', 'tourist', 'toward', 'tower', 'town', 'toy', 'track',
            'trade', 'traffic', 'tragic', 'train', 'transfer', 'trap', 'trash', 'travel', 'tray', 'treat', 'tree',
            'trend', 'trial', 'tribe', 'trick', 'trigger', 'trim', 'trip', 'trophy', 'trouble', 'truck', 'true',
            'truly', 'trumpet', 'trust', 'truth', 'try', 'tube', 'tuition', 'tumble', 'tuna', 'tunnel', 'turkey',
            'turn', 'turtle', 'twelve', 'twenty', 'twice', 'twin', 'twist', 'two', 'type', 'typical', 'ugly',
            'umbrella', 'unable', 'unaware', 'uncle', 'uncover', 'under', 'undo', 'unfair', 'unfold', 'unhappy',
            'uniform', 'unique', 'unit', 'universe', 'unknown', 'unlock', 'until', 'unusual', 'unveil', 'update',
            'upgrade', 'uphold', 'upon', 'upper', 'upset', 'urban', 'urge', 'usage', 'use', 'used', 'useful', 'useless',
            'usual', 'utility', 'vacant', 'vacuum', 'vague', 'valid', 'valley', 'valve', 'van', 'vanish', 'vapor',
            'various', 'vast', 'vault', 'vehicle', 'velvet', 'vendor', 'venture', 'venue', 'verb', 'verify', 'version',
            'very', 'vessel', 'veteran', 'viable', 'vibrant', 'vicious', 'victory', 'video', 'view', 'village',
            'vintage', 'violin', 'virtual', 'virus', 'visa', 'visit', 'visual', 'vital', 'vivid', 'vocal', 'voice',
            'void', 'volcano', 'volume', 'vote', 'voyage', 'wage', 'wagon', 'wait', 'walk', 'wall', 'walnut', 'want',
            'warfare', 'warm', 'warrior', 'wash', 'wasp', 'waste', 'water', 'wave', 'way', 'wealth', 'weapon', 'wear',
            'weasel', 'weather', 'web', 'wedding', 'weekend', 'weird', 'welcome', 'west', 'wet', 'whale', 'what',
            'wheat', 'wheel', 'when', 'where', 'whip', 'whisper', 'wide', 'width', 'wife', 'wild', 'will', 'win',
            'window', 'wine', 'wing', 'wink', 'winner', 'winter', 'wire', 'wisdom', 'wise', 'wish', 'witness', 'wolf',
            'woman', 'wonder', 'wood', 'wool', 'word', 'work', 'world', 'worry', 'worth', 'wrap', 'wreck', 'wrestle',
            'wrist', 'write', 'wrong', 'yard', 'year', 'yellow', 'you', 'young', 'youth', 'zebra', 'zero', 'zone',
            'zoo']

class Address(object):
    def __init__(self, address='', publicKey='', privateKey='', seed='', alias='', nonce=0):
        if nonce<0 or nonce>4294967295:
            raise ValueError('Nonce must be between 0 and 4294967295')
        if seed:
            self._generate(seed=seed, nonce=nonce)
        elif privateKey:
            self._generate(privateKey=privateKey)
        elif publicKey:
            self._generate(publicKey=publicKey)
        elif address:
            if not pywaves.validateAddress(address):
                raise ValueError("Invalid address")
            else:
                self.address = address
                self.publicKey = publicKey
                self.privateKey = privateKey
                self.seed = seed
                self.nonce = nonce
        elif alias and not pywaves.OFFLINE:
            self.address = pywaves.wrapper('/alias/by-alias/%s' % alias).get("address", "")
            self.publicKey = ''
            self.privateKey = ''
            self.seed = ''
            self.nonce = 0
        else:
            self._generate(nonce=nonce)
        if not pywaves.OFFLINE:
            self.aliases = self.aliases()

    def __str__(self):
        if self.address:
            ab = []
            try:
                assets_balances = pywaves.wrapper('/assets/balance/%s' % self.address)['balances']
                for a in assets_balances:
                    if a['balance'] > 0:
                        ab.append("  %s (%s) = %d" % (a['assetId'], a['issueTransaction']['name'].encode('ascii', 'ignore'), a['balance']))
            except:
                pass
            return 'address = %s\npublicKey = %s\nprivateKey = %s\nseed = %s\nnonce = %d\nbalances:\n  Waves = %d%s' % (self.address, self.publicKey, self.privateKey, self.seed, self.nonce, self.balance(), '\n'+'\n'.join(ab) if ab else '')

    __repr__ = __str__

    def balance(self, assetId='', confirmations=0):
        try:
            if assetId:
                return pywaves.wrapper('/assets/balance/%s/%s' % (self.address, assetId))['balance']
            else:
                return pywaves.wrapper('/addresses/balance/%s%s' % (self.address, '' if confirmations==0 else '/%d' % confirmations))['balance']
        except:
            return 0

    def assets(self):
        req = pywaves.wrapper('/assets/balance/%s' % self.address)['balances']
        return [r['assetId'] for r in req]

    def aliases(self):
        a = pywaves.wrapper('/alias/by-address/%s' % self.address)
        if type(a)==list:
            for i in range(len(a)):
                a[i] = a[i][8:]
        return a

    def _generate(self, publicKey='', privateKey='', seed='', nonce=0):
        self.seed = seed
        self.nonce = nonce
        if not publicKey and not privateKey and not seed:
            wordCount = 2048
            words = []
            for i in range(5):
                r = crypto.bytes2str(os.urandom(4))
                x = (ord(r[3])) + (ord(r[2]) << 8) + (ord(r[1]) << 16) + (ord(r[0]) << 24)
                w1 = x % wordCount
                w2 = ((int(x / wordCount) >> 0) + w1) % wordCount
                w3 = ((int((int(x / wordCount) >> 0) / wordCount) >> 0) + w2) % wordCount
                words.append(wordList[w1])
                words.append(wordList[w2])
                words.append(wordList[w3])
            self.seed = ' '.join(words)
        if publicKey:
            pubKey = base58.b58decode(publicKey)
            privKey = ""
        else:
            seedHash = crypto.hashChain(struct.pack(">L", nonce) + crypto.str2bytes(self.seed))
            accountSeedHash = crypto.sha256(seedHash)
            if not privateKey:
                privKey = curve.generatePrivateKey(accountSeedHash)
            else:
                privKey = base58.b58decode(privateKey)
            pubKey = curve.generatePublicKey(privKey)
        unhashedAddress = chr(1) + str(pywaves.CHAIN_ID) + crypto.hashChain(pubKey)[0:20]
        addressHash = crypto.hashChain(crypto.str2bytes(unhashedAddress))[0:4]
        self.address = base58.b58encode(crypto.str2bytes(unhashedAddress + addressHash))
        self.publicKey = base58.b58encode(pubKey)
        if privKey != "":
            self.privateKey = base58.b58encode(privKey)

    def issueAsset(self, name, description, quantity, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(name) < 4 or len(name) > 16:
            msg = 'Asset name must be between 4 and 16 characters long'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            timestamp = int(time.time() * 1000)
            sData = b'\3' + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">H", len(name)) + \
                    crypto.str2bytes(name) + \
                    struct.pack(">H", len(description)) + \
                    crypto.str2bytes(description) + \
                    struct.pack(">Q", quantity) + \
                    struct.pack(">B", decimals) + \
                    (b'\1' if reissuable else b'\0') + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature=crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "name": name,
                "quantity": quantity,
                "timestamp": timestamp,
                "description": description,
                "decimals": decimals,
                "reissuable": reissuable,
                "fee": txFee,
                "signature": signature
            })
            req = pywaves.wrapper('/assets/broadcast/issue', data)
            if pywaves.OFFLINE:
                return req
            else:
                return pywaves.Asset(req['assetId'])

    def reissueAsset(self, Asset, quantity, reissuable=False, txFee=pywaves.DEFAULT_TX_FEE):
        timestamp = int(time.time() * 1000)
        sData = b'\5' + \
                base58.b58decode(self.publicKey) + \
                base58.b58decode(Asset.assetId) + \
                struct.pack(">Q", quantity) + \
                (b'\1' if reissuable else b'\0') + \
                struct.pack(">Q",txFee) + \
                struct.pack(">Q", timestamp)
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "assetId": Asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "reissuable": reissuable,
            "fee": txFee,
            "signature": signature
        })
        req = pywaves.wrapper('/assets/broadcast/reissue', data)
        if pywaves.OFFLINE:
            return req
        else:
            return req.get('id', 'ERROR')

    def burnAsset(self, Asset, quantity, txFee=pywaves.DEFAULT_TX_FEE):
        timestamp = int(time.time() * 1000)

        sData = '\6' + \
                crypto.bytes2str(base58.b58decode(self.publicKey)) + \
                crypto.bytes2str(base58.b58decode(Asset.assetId)) + \
                crypto.bytes2str(struct.pack(">Q", quantity)) + \
                crypto.bytes2str(struct.pack(">Q", txFee)) + \
                crypto.bytes2str(struct.pack(">Q", timestamp))
        signature = crypto.sign(self.privateKey, crypto.str2bytes(sData))
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "assetId": Asset.assetId,
            "quantity": quantity,
            "timestamp": timestamp,
            "fee": txFee,
            "signature": signature
        })
        req = pywaves.wrapper('/assets/broadcast/burn', data)
        if pywaves.OFFLINE:
            return req
        else:
            return req.get('id', 'ERROR')

    def sendWaves(self, recipient, amount, attachment='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)

        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < amount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)

        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\4' + \
                    base58.b58decode(self.publicKey) + \
                    b'\0\0' + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    base58.b58decode(recipient.address) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature
            })

            return pywaves.wrapper('/assets/broadcast/transfer', data)

    def massTransferWaves(self, transfers, attachment='', timestamp=0):
        txFee = 100000 + (math.ceil((len(transfers) + 1) / 2 - 0.5)) * 100000
        totalAmount = 0

        for i in range(0, len(transfers)):
            totalAmount += transfers[i]['amount']

        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(transfers) > 100:
            msg = 'Too many recipients'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < totalAmount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            transfersData = b''
            for i in range(0, len(transfers)):
                transfersData += base58.b58decode(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount'])
            sData = b'\x0b' + \
                    b'\1' + \
                    base58.b58decode(self.publicKey) + \
                    b'\0' + \
                    struct.pack(">H", len(transfers)) + \
                    transfersData + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)

            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 11,
                "version": 1,
                "assetId": "",
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "transfers": transfers,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def sendAsset(self, recipient, asset, amount, attachment='', feeAsset='', txFee=pywaves.DEFAULT_TX_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Asset not issued'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and asset and not asset.status():
            msg = 'Asset not issued'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and asset and self.balance(asset.assetId) < amount:
            msg = 'Insufficient asset balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and not asset and self.balance() < amount:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and not feeAsset and self.balance() < txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and feeAsset and self.balance(feeAsset.assetId) < txFee:
            msg = 'Insufficient asset balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\4' + \
                    base58.b58decode(self.publicKey) + \
                    (b'\1' + base58.b58decode(asset.assetId) if asset else b'\0') + \
                    (b'\1' + base58.b58decode(feeAsset.assetId) if feeAsset else b'\0') + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    base58.b58decode(recipient.address) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "assetId": (asset.assetId if asset else ""),
                "feeAssetId": (feeAsset.assetId if feeAsset else ""),
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature
            })

            return pywaves.wrapper('/assets/broadcast/transfer', data)

    def massTransferAssets(self, transfers, asset, attachment='', timestamp=0):
        txFee = 100000 + (math.ceil((len(transfers) + 1) / 2 - 0.5)) * 100000

        totalAmount = 0

        if not self.privateKey:
            logging.error('Private key required')
        elif len(transfers) > 100:
            logging.error('Too many recipients')
        elif not pywaves.OFFLINE and self.balance() < txFee:
            logging.error('Insufficient Waves balance')
        elif not pywaves.OFFLINE and self.balance(assetId=asset.assetId) < totalAmount:
            logging.error('Insufficient %s balance' % asset.name)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            transfersData = b''
            for i in range(0, len(transfers)):
                transfersData += base58.b58decode(transfers[i]['recipient']) + struct.pack(">Q", transfers[i]['amount'])
            sData = b'\x0b' + \
                    b'\1' + \
                    base58.b58decode(self.publicKey) + \
                    b'\1' + \
                    base58.b58decode(asset.assetId) + \
                    struct.pack(">H", len(transfers)) + \
                    transfersData + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">H", len(attachment)) + \
                    crypto.str2bytes(attachment)

            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 11,
                "version": 1,
                "assetId": asset.assetId,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "transfers": transfers,
                "attachment": base58.b58encode(crypto.str2bytes(attachment)),
                "signature": signature,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def dataTransaction(self, data, timestamp=0):
        if not self.privateKey:
            logging.error('Private key required')
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            dataObject = {
                "type": 12,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "data": data,
                "fee": 0,
                "timestamp": timestamp,
                "proofs": ['']
            }
            dataBinary = b''
            for i in range(0, len(data)):
                d = data[i]
                keyBytes = crypto.str2bytes(d['key'])
                dataBinary += struct.pack(">H", len(keyBytes))
                dataBinary += keyBytes
                if d['type'] == 'binary':
                    dataBinary += b'\2'
                    valueAsBytes = d['value']
                    dataBinary += struct.pack(">H", len(valueAsBytes))
                    dataBinary += crypto.str2bytes(valueAsBytes)
                elif d['type'] == 'boolean':
                    if d['value']:
                        dataBinary += b'\1\1'
                    else:
                        dataBinary += b'\1\0'
                elif d['type'] == 'integer':
                    dataBinary += b'\0'
                    dataBinary += struct.pack(">Q", d['value'])
                elif d['type'] == 'string':
                    dataBinary += b'\3'
                    dataBinary += struct.pack(">H", len(d['value']))
                    dataBinary += crypto.str2bytes(d['value'])
            # check: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
            txFee = (int(( (len(crypto.str2bytes(json.dumps(data))) + 2 + 64 )) / 1000.0) + 1 ) * 100000
            dataObject['fee'] = txFee
            sData = b'\x0c' + \
                    b'\1' + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">H", len(data)) + \
                    dataBinary + \
                    struct.pack(">Q", timestamp) + \
                    struct.pack(">Q", txFee)

            dataObject['proofs'] = [ crypto.sign(self.privateKey, sData) ]

            for entry in dataObject['data']:
                if entry['type'] == 'binary':
                    base64Encoded =  base64.b64encode(crypto.str2bytes(entry['value']))
                    entry['value'] = 'base64:' + crypto.bytes2str(base64Encoded)
            dataObjectJSON = json.dumps(dataObject)
            return pywaves.wrapper('/transactions/broadcast', dataObjectJSON)

    def _postOrder(self, amountAsset, priceAsset, orderType, amount, price, maxLifetime=30*86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        expiration = timestamp + maxLifetime * 1000
        asset1 = b'\0' if amountAsset.assetId=='' else b'\1' + base58.b58decode(amountAsset.assetId)
        asset2 = b'\0' if priceAsset.assetId=='' else b'\1' + base58.b58decode(priceAsset.assetId)
        sData = base58.b58decode(self.publicKey) + \
                base58.b58decode(pywaves.MATCHER_PUBLICKEY) + \
                asset1 + \
                asset2 + \
                orderType + \
                struct.pack(">Q", price) + \
                struct.pack(">Q", amount) + \
                struct.pack(">Q", timestamp) + \
                struct.pack(">Q", expiration) + \
                struct.pack(">Q", matcherFee)
        signature = crypto.sign(self.privateKey, sData)
        otype = "buy" if orderType==b'\0' else "sell"
        data = json.dumps({
            "senderPublicKey": self.publicKey,
            "matcherPublicKey": pywaves.MATCHER_PUBLICKEY,
            "assetPair": {
                "amountAsset": amountAsset.assetId,
                "priceAsset": priceAsset.assetId,
                },
            "orderType": otype,
            "price": price,
            "amount": amount,
            "timestamp": timestamp,
            "expiration": expiration,
            "matcherFee": matcherFee,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook', data, host=pywaves.MATCHER)
        id = -1
        if 'status' in req:
            if req['status'] == 'OrderRejected':
                msg = 'Order Rejected - %s' % req['message']
                logging.error(msg)
                pywaves.throw_error(msg)
            elif req['status'] == 'OrderAccepted':
                id = req['message']['id']
                logging.info('Order Accepted - ID: %s' % id)
        elif not pywaves.OFFLINE:
            logging.error(req)
            pywaves.throw_error(req)
        else:
            return req
        return id

    def cancelOrder(self, assetPair, order):
        if not pywaves.OFFLINE:
            if order.status() == 'Filled':
                msg = "Order already filled"
                logging.error(msg)
                pywaves.throw_error(msg)

            elif not order.status():
                msg = "Order not found"
                logging.error(msg)
                pywaves.throw_error(msg)
        sData = base58.b58decode(self.publicKey) + \
                base58.b58decode(order.orderId)
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "sender": self.publicKey,
            "orderId": order.orderId,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)
        if pywaves.OFFLINE:
            return req
        else:
            id = -1
            if req['status'] == 'OrderCanceled':
                id = req['orderId']
                logging.info('Order Cancelled - ID: %s' % id)
            return id

    def cancelOrderByID(self, assetPair, orderId):
        sData = base58.b58decode(self.publicKey) + \
                base58.b58decode(orderId)
        signature = crypto.sign(self.privateKey, sData)
        data = json.dumps({
            "sender": self.publicKey,
            "orderId": orderId,
            "signature": signature
        })
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)
        if pywaves.OFFLINE:
            return req
        else:
            id = -1
            if req['status'] == 'OrderCanceled':
                id = req['orderId']
                logging.info('Order Cancelled - ID: %s' % id)
            return id

    def buy(self, assetPair, amount, price, maxLifetime=30 * 86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        assetPair.refresh()
        normPrice = int(pow(10, assetPair.asset2.decimals - assetPair.asset1.decimals) * price)
        id = self._postOrder(assetPair.asset1, assetPair.asset2, b'\0', amount, normPrice, maxLifetime, matcherFee, timestamp)
        if pywaves.OFFLINE:
            return id
        elif id != -1:
            return pywaves.Order(id, assetPair, self)

    def sell(self, assetPair, amount, price, maxLifetime=30 * 86400, matcherFee=pywaves.DEFAULT_MATCHER_FEE, timestamp=0):
        assetPair.refresh()
        normPrice = int(pow(10, assetPair.asset2.decimals - assetPair.asset1.decimals) * price)
        id = self._postOrder(assetPair.asset1, assetPair.asset2, b'\1', amount, normPrice, maxLifetime, matcherFee, timestamp)
        if pywaves.OFFLINE:
            return id
        elif id!=-1:
            return pywaves.Order(id, assetPair, self)

    def tradableBalance(self, assetPair):
        try:
            req = pywaves.wrapper('/matcher/orderbook/%s/%s/tradableBalance/%s' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId, self.address), host=pywaves.MATCHER)
            if pywaves.OFFLINE:
                    return req
            amountBalance = req['WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId]
            priceBalance = req['WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId]
        except:
            amountBalance = 0
            priceBalance = 0
        if not pywaves.OFFLINE:
            return amountBalance, priceBalance

    def lease(self, recipient, amount, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif amount <= 0:
            msg = 'Amount must be > 0'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < amount + txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x08' + \
                    base58.b58decode(self.publicKey) + \
                    base58.b58decode(recipient.address) + \
                    struct.pack(">Q", amount) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "recipient": recipient.address,
                "amount": amount,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            req = pywaves.wrapper('/leasing/broadcast/lease', data)
            return req

    def leaseCancel(self, leaseId, txFee=pywaves.DEFAULT_LEASE_FEE, timestamp=0):
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif not pywaves.OFFLINE and self.balance() < txFee:
            msg = 'Insufficient Waves balance'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x09' + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp) + \
                    base58.b58decode(leaseId)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "senderPublicKey": self.publicKey,
                "txId": leaseId,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            req = pywaves.wrapper('/leasing/broadcast/cancel', data)
            if pywaves.OFFLINE:
                return req
            elif 'leaseId' in req:
                return req['leaseId']

    def getOrderHistory(self, assetPair, timestamp=0):
        if timestamp == 0:
            timestamp = int(time.time() * 1000)
        sData = base58.b58decode(self.publicKey) + \
                struct.pack(">Q", timestamp)
        signature = crypto.sign(self.privateKey, sData)
        data = {
            "Accept": "application/json",
            "Timestamp": str(timestamp),
            "Signature": signature
        }
        req = pywaves.wrapper('/matcher/orderbook/%s/%s/publicKey/%s' % ('WAVES' if assetPair.asset1.assetId=='' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId=='' else assetPair.asset2.assetId, self.publicKey), headers=data, host=pywaves.MATCHER)
        return req

    def cancelOpenOrders(self, assetPair):
        orders = self.getOrderHistory(assetPair)
        for order in orders:
            status = order['status']
            orderId = order['id']
            if status=='Accepted' or status=='PartiallyFilled':
                sData = base58.b58decode(self.publicKey) + \
                        base58.b58decode(orderId)
                signature = crypto.sign(self.privateKey, sData)
                data = json.dumps({
                    "sender": self.publicKey,
                    "orderId": orderId,
                    "signature": signature
                })
                pywaves.wrapper('/matcher/orderbook/%s/%s/cancel' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)

    def deleteOrderHistory(self, assetPair):
        orders = self.getOrderHistory(assetPair)
        for order in orders:
            orderId = order['id']
            sData = base58.b58decode(self.publicKey) + \
                    base58.b58decode(orderId)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "sender": self.publicKey,
                "orderId": orderId,
                "signature": signature
            })
            pywaves.wrapper('/matcher/orderbook/%s/%s/delete' % ('WAVES' if assetPair.asset1.assetId == '' else assetPair.asset1.assetId, 'WAVES' if assetPair.asset2.assetId == '' else assetPair.asset2.assetId), data, host=pywaves.MATCHER)

    def createAlias(self, alias, txFee=pywaves.DEFAULT_ALIAS_FEE, timestamp=0):
        aliasWithNetwork = b'\x02' + crypto.str2bytes(str(pywaves.CHAIN_ID)) + struct.pack(">H", len(alias)) + crypto.str2bytes(alias)
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0a' + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">H", len(aliasWithNetwork)) + \
                    crypto.str2bytes(str(aliasWithNetwork)) + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "alias": alias,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "signature": signature
            })
            return pywaves.wrapper('/alias/broadcast/create', data)

    def sponsorAsset(self, assetId, minimalFeeInAssets, txFee=pywaves.DEFAULT_SPONSOR_FEE, timestamp=0):
        if not self.privateKey:
            logging.error('Private key required')
        else:
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0e' + \
                b'\1' + \
                base58.b58decode(self.publicKey) + \
                base58.b58decode(assetId) + \
                struct.pack(">Q", minimalFeeInAssets) + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 14,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "assetId": assetId,
                "fee": txFee,
                "timestamp": timestamp,
                "minSponsoredAssetFee": minimalFeeInAssets,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def setScript(self, scriptSource, txFee=pywaves.DEFAULT_SCRIPT_FEE, timestamp=0):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            logging.error('Private key required')
        else:
            compiledScript = base64.b64decode(script)
            scriptLength = len(compiledScript)
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0d' + \
                b'\1' + \
                crypto.str2bytes(str(pywaves.CHAIN_ID)) + \
                base58.b58decode(self.publicKey) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp)
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 13,
                "version": 1,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "script": 'base64:' + script,
                "proofs": [
                    signature
                ]
            })

            return pywaves.wrapper('/transactions/broadcast', data)

    def setAssetScript(self, asset, scriptSource, txFee=pywaves.DEFAULT_ASSET_SCRIPT_FEE, timestamp=0):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            logging.error('Private key required')
        else:
            compiledScript = base64.b64decode(script)
            scriptLength = len(compiledScript)
            if timestamp == 0:
                timestamp = int(time.time() * 1000)
            sData = b'\x0f' + \
                b'\1' + \
                crypto.str2bytes(str(pywaves.CHAIN_ID)) + \
                base58.b58decode(self.publicKey) + \
                base58.b58decode(asset.assetId) + \
                struct.pack(">Q", txFee) + \
                struct.pack(">Q", timestamp) + \
                b'\1' + \
                struct.pack(">H", scriptLength) + \
                compiledScript
            signature = crypto.sign(self.privateKey, sData)

            data = json.dumps({
                "type": 15,
                "version": 1,
                "assetId": asset.assetId,
                "senderPublicKey": self.publicKey,
                "fee": txFee,
                "timestamp": timestamp,
                "script": 'base64:' + script,
                "proofs": [
                    signature
                ]
            })
            print(data)

            return pywaves.wrapper('/transactions/broadcast', data)

    def issueSmartAsset(self, name, description, quantity, scriptSource, decimals=0, reissuable=False, txFee=pywaves.DEFAULT_ASSET_FEE):
        script = pywaves.wrapper('/utils/script/compile', scriptSource)['script'][7:]
        if not self.privateKey:
            msg = 'Private key required'
            logging.error(msg)
            pywaves.throw_error(msg)
        elif len(name) < 4 or len(name) > 16:
            msg = 'Asset name must be between 4 and 16 characters long'
            logging.error(msg)
            pywaves.throw_error(msg)
        else:
            compiledScript = base64.b64decode(script)
            scriptLength = len(compiledScript)
            timestamp = int(time.time() * 1000)
            sData = b'\3' + \
                    b'\2' + \
                    crypto.str2bytes(str(pywaves.CHAIN_ID)) + \
                    base58.b58decode(self.publicKey) + \
                    struct.pack(">H", len(name)) + \
                    crypto.str2bytes(name) + \
                    struct.pack(">H", len(description)) + \
                    crypto.str2bytes(description) + \
                    struct.pack(">Q", quantity) + \
                    struct.pack(">B", decimals) + \
                    (b'\1' if reissuable else b'\0') + \
                    struct.pack(">Q", txFee) + \
                    struct.pack(">Q", timestamp) + \
                    b'\1' + \
                    struct.pack(">H", scriptLength) + \
                    compiledScript
            signature = crypto.sign(self.privateKey, sData)
            data = json.dumps({
                "type": 3,
                "senderPublicKey": self.publicKey,
                "name": name,
                "version": 2,
                "quantity": quantity,
                "timestamp": timestamp,
                "description": description,
                "decimals": decimals,
                "reissuable": reissuable,
                "fee": txFee,
                "proofs": [ signature ],
                "script": 'base64:' + script
            })
            print(data)
            req = pywaves.wrapper('/transactions/broadcast', data)
            if pywaves.OFFLINE:
                return req
            else:
                return req
