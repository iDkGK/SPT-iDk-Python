import builtins as b
import colorama as ca
import copy as cp
import datetime as dt
import hashlib as hl
import http as h
import http.client as hcl
import http.cookies as hck
import http.server as hsv
import importlib.machinery as im
import io as io
import math as m
import orjson as js
import os as os
import random as ra
import re as re
import shutil as sh
import socket as sk
import sys as sys
import threading as th
import time as t
import traceback as tb
import websocket_server as wsv
import zlib as zl


class server():

    class bindings:

        class initializefunctions:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getfunctions():
                return {
                    'config': configcallbacks.init,
                    'database': databasecallbacks.init,
                    'handbook': handbookcallbacks.init,
                    'http': httpcallbacks.init,
                    'preset': presetcallbacks.init,
                    'ragfair': ragfaircallbacks.init,
                    'save': savecallbacks.init,
                    'traders': tradercallbacks.init,
                }

        class updatefunctions:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getfunctions():
                return {
                    'dialogue': dialoguecallbacks.update,
                    'hideout': hideoutcallbacks.update,
                    'insurance': insurancecallbacks.update,
                    'ragfair': ragfaircallbacks.update,
                    'traders': tradercallbacks.update,
                    'save': savecallbacks.update
                }

        class saveinitfunctions:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getfunctions():
                return {
                    'health': healthcallbacks.init,
                    'inraid': inraidcallbacks.init,
                    'insurance': insurancecallbacks.init,
                    'profile': profilecallbacks.init
                }

        class staticroutes:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getroutes():
                return {
                    '/launcher/server/connect': {
                        'aki': launchercallbacks.connect
                    },
                    '/launcher/profile/register': {
                        'aki': launchercallbacks.register
                    },
                    '/launcher/profile/login': {
                        'aki': launchercallbacks.login
                    },
                    '/launcher/profile/get': {
                        'aki': launchercallbacks.get
                    },
                    '/launcher/profile/info': {
                        'aki': launchercallbacks.getinfo
                    },
                    '/launcher/profile/change/username': {
                        'aki': launchercallbacks.changeusername
                    },
                    '/launcher/profile/change/password': {
                        'aki': launchercallbacks.changepassword
                    },
                    '/launcher/profile/change/wipe': {
                        'aki': launchercallbacks.wipe
                    },
                    '/launcher/ping': {
                        'aki': launchercallbacks.ping
                    }
                }

        class dynamicroutes:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getroutes():
                return {
                    '.jpg': {
                        'aki': httpcallbacks.getimage
                    },
                    '.png': {
                        'aki': httpcallbacks.getimage
                    },
                    '.ico': {
                        'aki': httpcallbacks.getimage
                    },
                    '.bundle': {
                        'aki': None
                    }
                }

        class serverresponse:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getresponses():
                return {'IMAGE': httpcallbacks.sendimage}

        class itemevents:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getevents():
                return {
                    'CustomizationWear': {
                        'aki': None  #CustomizationCallbacks.wearClothing
                    },
                    'CustomizationBuy': {
                        'aki': None  #CustomizationCallbacks.buyClothing
                    },
                    'Eat': {
                        'aki': None  #HealthCallbacks.offraidEat
                    },
                    'Heal': {
                        'aki': None  #HealthCallbacks.offraidHeal
                    },
                    'RestoreHealth': {
                        'aki': None  #HealthCallbacks.healthTreatment
                    },
                    'HideoutUpgrade': {
                        'aki': None  #HideoutCallbacks.upgrade
                    },
                    'HideoutUpgradeComplete': {
                        'aki': None  #HideoutCallbacks.upgradeComplete
                    },
                    'HideoutPutItemsInAreaSlots': {
                        'aki': None  #HideoutCallbacks.putItemsInAreaSlots
                    },
                    'HideoutTakeItemsFromAreaSlots': {
                        'aki': None  #HideoutCallbacks.takeItemsFromAreaSlots
                    },
                    'HideoutToggleArea': {
                        'aki': None  #HideoutCallbacks.toggleArea
                    },
                    'HideoutSingleProductionStart': {
                        'aki': None  #HideoutCallbacks.singleProductionStart
                    },
                    'HideoutScavCaseProductionStart': {
                        'aki': None  #HideoutCallbacks.scavCaseProductionStart
                    },
                    'HideoutContinuousProductionStart': {
                        'aki':
                        None  #HideoutCallbacks.continuousProductionStart
                    },
                    'HideoutTakeProduction': {
                        'aki': None  #HideoutCallbacks.takeProduction
                    },
                    'Insure': {
                        'aki': None  #InsuranceCallbacks.insure
                    },
                    'Move': {
                        'aki': None  #InventoryCallbacks.moveItem
                    },
                    'Remove': {
                        'aki': None  #InventoryCallbacks.removeItem
                    },
                    'Split': {
                        'aki': None  #InventoryCallbacks.splitItem
                    },
                    'Merge': {
                        'aki': None  #InventoryCallbacks.mergeItem
                    },
                    'Transfer': {
                        'aki': None  #InventoryCallbacks.transferItem
                    },
                    'Swap': {
                        'aki': None  #InventoryCallbacks.swapItem
                    },
                    'Fold': {
                        'aki': None  #InventoryCallbacks.foldItem
                    },
                    'Toggle': {
                        'aki': None  #InventoryCallbacks.toggleItem
                    },
                    'Tag': {
                        'aki': None  #InventoryCallbacks.tagItem
                    },
                    'Bind': {
                        'aki': None  #InventoryCallbacks.bindItem
                    },
                    'Examine': {
                        'aki': None  #InventoryCallbacks.examineItem
                    },
                    'ReadEncyclopedia': {
                        'aki': None  #InventoryCallbacks.readEncyclopedia
                    },
                    'ApplyInventoryChanges': {
                        'aki': None  #InventoryCallbacks.sortInventory
                    },
                    'AddNote': {
                        'aki': None  #NoteCallbacks.addNote
                    },
                    'EditNote': {
                        'aki': None  #NoteCallbacks.editNote
                    },
                    'DeleteNote': {
                        'aki': None  #NoteCallbacks.deleteNote
                    },
                    'SaveBuild': {
                        'aki': None  #PresetBuildCallbacks.saveBuild
                    },
                    'RemoveBuild': {
                        'aki': None  #PresetBuildCallbacks.removeBuild
                    },
                    'QuestAccept': {
                        'aki': None  #QuestCallbacks.acceptQuest
                    },
                    'QuestComplete': {
                        'aki': None  #QuestCallbacks.completeQuest
                    },
                    'QuestHandover': {
                        'aki': None  #QuestCallbacks.handoverQuest
                    },
                    'RagFairAddOffer': {
                        'aki': None  #RagfairCallbacks.addOffer
                    },
                    'RagFairRemoveOffer': {
                        'aki': None  #RagfairCallbacks.removeOffer
                    },
                    'RagFairRenewOffer': {
                        'aki': None  #RagfairCallbacks.extendOffer
                    },
                    'Repair': {
                        'aki': None  #RepairCallbacks.repair
                    },
                    'TradingConfirm': {
                        'aki': None  #TradeCallbacks.processTrade
                    },
                    'RagFairBuyOffer': {
                        'aki': None  #TradeCallbacks.processRagfairTrade
                    },
                    'AddToWishList': {
                        'aki': None  #WishlistCallbacks.addToWishlist
                    },
                    'RemoveFromWishList': {
                        'aki': None  #WishlistCallbacks.removeFromWishlist
                    },
                    'CreateMapMarker': {
                        'aki': None  #InventoryCallbacks.createMapMarker
                    },
                    'DeleteMapMarker': {
                        'aki': None  #InventoryCallbacks.deleteMapMarker
                    },
                    'EditMapMarker': {
                        'aki': None  #InventoryCallbacks.editMapMarker
                    }
                }

    class callbacks:

        class botcallbacks:

            @staticmethod
            def init():
                pass

        class bundlecallbacks:

            @staticmethod
            def init():
                pass

        class configcallbacks:

            @staticmethod
            def init():
                botconfig.init()
                healthconfig.init()
                hideoutconfig.init()
                httpconfig.init()
                inraidconfig.init()
                insuranceconfig.init()
                inventoryconfig.init()
                locationconfig.init()
                matchconfig.init()
                projectconfig.init()
                questconfig.init()
                ragfairconfig.init()
                repairconfig.init()
                saveconfig.init()
                traderconfig.init()
                weatherconfig.init()

        class customizationcallbacks:

            @staticmethod
            def init():
                pass

        class databasecallbacks:

            @staticmethod
            def init():
                databaseutil.init()

        class dialoguecallbacks:

            @staticmethod
            def init():
                pass

            def update(interval):
                return True

        class gamecallbacks:

            @staticmethod
            def init():
                pass

        class handbookcallbacks:

            @staticmethod
            def init():
                handbookcontroller.init()

        class healthcallbacks:

            @staticmethod
            def init(ssid):
                healthcontroller.init(ssid)

        class hideoutcallbacks:

            @staticmethod
            def init():
                pass

            def update(interval):
                if interval < hideoutconfig.runInterval:
                    return False
                return True

        class httpcallbacks:

            @staticmethod
            def init():
                imagerouter.init()
                itemeventrouter.init()
                httprouter.init()
                httpserver.init()

            @staticmethod
            def sendimage(ssid, url, body, result, resp):
                imagerouter.sendimage(ssid, url, body, result, resp)

            @staticmethod
            def getimage(ssid, url, body, result, resp):
                return imagerouter.getimage(ssid, url, body, result, resp)

        class inraidcallbacks:

            @staticmethod
            def init(ssid):
                inraidcontroller.init(ssid)

        class insurancecallbacks:

            @staticmethod
            def init(ssid):
                insurancecontroller.init(ssid)

            def update(interval):
                if interval < insuranceconfig.runInterval:
                    return False
                return True

        class inventorycallbacks:

            @staticmethod
            def init():
                pass

        class itemeventcallbacks:

            @staticmethod
            def init():
                pass

        class launchercallbacks:

            @staticmethod
            def init():
                pass

            @staticmethod
            def connect(ssid, url, body, result, resp):
                return httputil.getnobody({
                    'backendUrl':
                    httpserver.getbackendurl(),
                    'name':
                    ' '.join([watermarkutil.name, watermarkutil.version]),
                    'editions':
                    list(databaseserver.tables['templates']['profiles'].keys())
                })

            @staticmethod
            def register(ssid, url, body, result, resp):
                result = launchercontroller.register(body)
                if not result:
                    return 'FAILED'
                return 'OK'

            @staticmethod
            def login(ssid, url, body, result, resp):
                result = launchercontroller.login(body)
                if not result:
                    return 'FAILED'
                return result

            @staticmethod
            def get(ssid, url, body, result, resp):
                return httputil.getnobody(
                    launchercontroller.find(launchercontroller.login(body)))

            @staticmethod
            def getinfo(ssid, url, body, result, resp):
                return httputil.getnobody(
                    profilecontroller.getminiprofile(ssid))

            @staticmethod
            def changeusername(ssid, url, body, result, resp):
                pass

            @staticmethod
            def changepassword(ssid, url, body, result, resp):
                pass

            @staticmethod
            def wipe(ssid, url, body, result, resp):
                pass

            @staticmethod
            def ping(ssid, url, body, result, resp):
                pass

        class locationcallbacks:

            @staticmethod
            def init():
                pass

        class classname:

            @staticmethod
            def init():
                pass

        class matchcallbacks:

            @staticmethod
            def init():
                pass

        class notecallbacks:

            @staticmethod
            def init():
                pass

        class notifiercallbacks:

            @staticmethod
            def init():
                pass

        class presetbuildcallbacks:

            @staticmethod
            def init():
                pass

        class presetcallbacks:

            @staticmethod
            def init():
                presetcontroller.init()

        class profilecallbacks:

            @staticmethod
            def init(ssid):
                profilecontroller.init(ssid)

        class questcallbacks:

            @staticmethod
            def init():
                pass

        class ragfaircallbacks:

            @staticmethod
            def init():
                ragfairserver.init()

            def update(interval):
                return True

        class repaircallbacks:

            @staticmethod
            def init():
                pass

        class savecallbacks:

            @staticmethod
            def init():
                saveserver.init()

            def update(interval):
                if interval < saveconfig.runInterval:
                    return False
                return saveserver.save()

        class tradecallbacks:

            @staticmethod
            def init():
                pass

        class tradercallbacks:

            @staticmethod
            def init():
                pass

            def update(interval):
                return True

        class weathercallbacks:

            @staticmethod
            def init():
                pass

        class wishlistcallbacks:

            @staticmethod
            def init():
                pass

    class configs:

        class botconfig:
            presetBatch = {}
            bosses = []
            durability = {}
            pmc = {}
            showTypeInNickname = None
            maxBotCap = None

            @staticmethod
            def init():
                botconfig.presetBatch = {
                    'assault': 120,
                    'bossBully': 1,
                    'bossGluhar': 1,
                    'bossKilla': 1,
                    'bossKojaniy': 1,
                    'bossSanitar': 1,
                    'bossTagilla': 1,
                    'bossTest': 40,
                    'cursedAssault': 120,
                    'followerBully': 4,
                    'followerGluharAssault': 2,
                    'followerGluharScout': 2,
                    'followerGluharSecurity': 2,
                    'followerGluharSnipe': 2,
                    'followerKojaniy': 2,
                    'followerSanitar': 2,
                    'followerTagilla': 2,
                    'followerTest': 4,
                    'marksman': 30,
                    'pmcBot': 120,
                    'sectantPriest': 1,
                    'sectantWarrior': 5,
                    'gifter': 1,
                    'test': 40,
                    'exUsec': 15
                }
                botconfig.bosses = [
                    'bossbully', 'bossgluhar', 'bosskilla', 'bosskojaniy',
                    'bosssanitar', 'bosstagilla'
                ]
                botconfig.durability = {
                    'pmcbot': {
                        'armor': {
                            'minPercent': 80
                        },
                        'weapon': {
                            'minPercent': 80
                        }
                    },
                    'exusec': {
                        'armor': {
                            'minPercent': 80
                        },
                        'weapon': {
                            'minPercent': 80
                        }
                    },
                    'pmc': {
                        'armor': {
                            'minPercent': 80
                        },
                        'weapon': {
                            'minPercent': 80
                        }
                    },
                    'boss': {
                        'armor': {
                            'minPercent': 80
                        },
                        'weapon': {
                            'minPercent': 80
                        }
                    }
                }
                botconfig.pmc = {
                    'dynamicLoot': {
                        'whitelist': [
                            itemhelper.BASECLASS()['Jewelry'],
                            itemhelper.BASECLASS()['Electronics'],
                            itemhelper.BASECLASS()['BuildingMaterial'],
                            itemhelper.BASECLASS()['Tool'],
                            itemhelper.BASECLASS()['HouseholdGoods'],
                            itemhelper.BASECLASS()['MedicalSupplies'],
                            itemhelper.BASECLASS()['Lubricant'],
                            itemhelper.BASECLASS()['Battery'],
                            itemhelper.BASECLASS()['Keycard'],
                            itemhelper.BASECLASS()['KeyMechanical'],
                            itemhelper.BASECLASS()['AssaultScope'],
                            itemhelper.BASECLASS()['ReflexSight'],
                            itemhelper.BASECLASS()['TacticalCombo'],
                            itemhelper.BASECLASS()['Magazine'],
                            itemhelper.BASECLASS()['Knife'],
                            itemhelper.BASECLASS()['BarterItem'],
                            itemhelper.BASECLASS()['Silencer'],
                            itemhelper.BASECLASS()['Foregrip'],
                            itemhelper.BASECLASS()['Info'],
                            itemhelper.BASECLASS()['Food'],
                            itemhelper.BASECLASS()['Drink'],
                            itemhelper.BASECLASS()['Drugs'],
                            itemhelper.BASECLASS()['Armor'],
                            itemhelper.BASECLASS()['Stimulator'],
                            itemhelper.BASECLASS()['AmmoBox'],
                            itemhelper.BASECLASS()['Money'],
                            itemhelper.BASECLASS()['Other']
                        ],
                        'blacklist': [
                            '5fca13ca637ee0341a484f46',
                            '59f32c3b86f77472a31742f0',
                            '59f32bb586f774757e1e8442',
                            '6087e570b998180e9f76dc24'
                        ],
                        'spawnLimits': {
                            '5c99f98d86f7745c314214b3': 1,
                            '5c164d2286f774194c5e69fa': 1,
                            '550aa4cd4bdc2dd8348b456c': 2,
                            '55818add4bdc2d5b648b456f': 1,
                            '55818ad54bdc2ddc698b4569': 1,
                            '55818af64bdc2d5b648b4570': 1,
                            '5448e54d4bdc2dcc718b4568': 1,
                            '5448f3a64bdc2d60728b456a': 2,
                            '5447e1d04bdc2dff2f8b4567': 1,
                            '5a341c4686f77469e155819e': 1,
                            '55818b164bdc2ddc698b456c': 2,
                            '5448bc234bdc2d3c308b4569': 2,
                            '543be5dd4bdc2deb348b4569': 2,
                            '543be5cb4bdc2deb348b4568': 2
                        },
                        'moneyStackLimits': {
                            '5449016a4bdc2d6f028b456f': 4000,
                            '5696686a4bdc2da3298b456a': 50,
                            '569668774bdc2da2298b4568': 50
                        }
                    },
                    'difficulty': 'AsOnline',
                    'isUsec': 50,
                    'chanceSameSideIsHostilePercent': 50,
                    'usecType': 'bosstest',
                    'bearType': 'test',
                    'maxLootTotalRub': 150000,
                    'types': {
                        'assault': 35,
                        'cursedAssault': 35,
                        'pmcBot': 35
                    }
                }
                botconfig.showTypeInNickname = False
                botconfig.maxBotCap = 20

        class healthconfig:
            healthMultipliers = {}
            save = {}

            @staticmethod
            def init():
                healthconfig.healthMultipliers = {'death': 0.3, 'blacked': 0.1}
                healthconfig.save = {'health': True, 'effects': True}

        class hideoutconfig:
            runInterval = None

            @staticmethod
            def init():
                hideoutconfig.runInterval = 1

        class httpconfig:
            ip = None
            port = None

            @staticmethod
            def init():
                httpconfig.ip = '127.0.0.1'
                httpconfig.port = 6969

        class inraidconfig:
            MIAOnRaidEnd = None
            raidMenuSettings = {}
            save = {}
            carExtracts = []
            carExtractBaseStandingGain = None
            scavExtractGain = None

            @staticmethod
            def init():
                inraidconfig.MIAOnRaidEnd = True
                inraidconfig.raidMenuSettings = {
                    'aiAmount': 'AsOnline',
                    'aiDifficulty': 'AsOnline',
                    'bossEnabled': True,
                    'scavWars': False,
                    'taggedAndCursed': False
                }
                inraidconfig.save = {'loot': True, 'durability': True}
                inraidconfig.carExtracts = [
                    'Dorms V-Ex', 'PP Exfil', ' V-Ex_light', 'South V-Ex'
                ]
                inraidconfig.carExtractBaseStandingGain = 0.25
                inraidconfig.scavExtractGain = 0.01

        class insuranceconfig:
            insuranceMultiplier = {}
            returnChance = None
            runInterval = None

            @staticmethod
            def init():
                insuranceconfig.insuranceMultiplier = {
                    '54cb50c76803fa8b248b4571': 0.16,
                    '54cb57776803fa99248b456e': 0.25
                }
                insuranceconfig.returnChance = 80
                insuranceconfig.runInterval = 1

        class inventoryconfig:
            newItemsMarkedFound = None

            @staticmethod
            def init():
                inventoryconfig.newItemsMarkedFound = False

        class locationconfig:
            allowLootOverlay = None
            limits = None

            @staticmethod
            def init():
                locationconfig.allowLootOverlay = False
                locationconfig.limits = {
                    'bigmap': 1000,
                    'develop': 30,
                    'factory4_day': 100,
                    'factory4_night': 100,
                    'interchange': 2000,
                    'laboratory': 1000,
                    'rezervbase': 3000,
                    'shoreline': 1000,
                    'woods': 200,
                    'hideout': 0,
                    'lighthouse': 1500,
                    'privatearea': 0,
                    'suburbs': 0,
                    'tarkovstreets': 0,
                    'terminal': 0,
                    'town': 0
                }

        class matchconfig:
            enabled = None

            @staticmethod
            def init():
                matchconfig.enabled = False

        class projectconfig:
            projectVersion = None
            projectName = None

            @staticmethod
            def init():
                projectconfig.projectVersion = '1.0.0'
                projectconfig.projectName = 'SPT-iDk Python'

        class questconfig:
            redeemTime = None
            repeatableQuests = None

            @staticmethod
            def init():
                questconfig.redeemTime = 48,
                questconfig.repeatableQuests = [
                    {
                        'name': 'Daily',
                        'types': ['Elimination', 'Completion', 'Exploration'],
                        'resetTime': 60 * 60 * 24,
                        'numQuests': 3,
                        'minPlayerLevel': 5,
                        'rewardScaling': {
                            'levels': [1, 20, 45, 100],
                            'experience': [2000, 4000, 20000, 80000],
                            'roubles': [6000, 10000, 100000, 250000],
                            'items': [1, 2, 4, 4],
                            'reputation': [0.01, 0.01, 0.01, 0.01],
                            'rewardSpread': 0.5
                        },
                        'locations': {
                            'any': ['any'],
                            'factory4_day': ['factory4_day', 'factory4_night'],
                            'bigmap': ['bigmap'],
                            'Woods': ['Woods'],
                            'Shoreline': ['Shoreline'],
                            'Interchange': ['Interchange'],
                            'Lighthouse': ['Lighthouse'],
                            'laboratory': ['laboratory'],
                            'RezervBase': ['RezervBase']
                        },
                        'questConfig': {
                            'Exploration': {
                                'maxExtracts': 3,
                                'specificExits': {
                                    'probability':
                                    0.25,
                                    'passageRequirementWhitelist': [
                                        'None', 'TransferItem', 'WorldEvent',
                                        'Train', 'Reference', 'Empty'
                                    ]
                                }
                            },
                            'Completion': {
                                'minRequestedAmount': 1,
                                'maxRequestedAmount': 5,
                                'minRequestedBulletAmount': 20,
                                'maxRequestedBulletAmount': 60,
                                'useWhitelist': True,
                                'useBlacklist': False,
                            },
                            'Elimination': {
                                'targets':
                                None,  #__REPLACEME__
                                'bodyPartProb':
                                0.4,
                                'bodyParts':
                                None,  #__REPLACEME__
                                'specificLocationProb':
                                0.25,
                                'distLocationBlacklist': [
                                    'laboratory', 'factory4_day',
                                    'factory4_night'
                                ],
                                'distProb':
                                0.25,
                                'maxDist':
                                200,
                                'minDist':
                                20,
                                'maxKills':
                                5,
                                'minKills':
                                2
                            }
                        }
                    },
                    {
                        'name': 'Weekly',
                        'types': ['Elimination', 'Completion', 'Exploration'],
                        'resetTime': 7 * 60 * 60 * 24,
                        'numQuests': 1,
                        'minPlayerLevel': 15,
                        'rewardScaling': {
                            'levels': [1, 20, 45, 100],
                            'experience': [4000, 8000, 40000, 160000],
                            'roubles': [12000, 20000, 200000, 500000],
                            'items': [3, 3, 4, 4],
                            'reputation': [0.02, 0.03, 0.03, 0.03],
                            'rewardSpread': 0.5
                        },
                        'locations': {
                            'any': ['any'],
                            'factory4_day': ['factory4_day', 'factory4_night'],
                            'bigmap': ['bigmap'],
                            'Woods': ['Woods'],
                            'Shoreline': ['Shoreline'],
                            'Interchange': ['Interchange'],
                            'Lighthouse': ['Lighthouse'],
                            'laboratory': ['laboratory'],
                            'RezervBase': ['RezervBase']
                        },
                        'questConfig': {
                            'Exploration': {
                                'maxExtracts': 10,
                                'specificExits': {
                                    'probability':
                                    0.5,
                                    'passageRequirementWhitelist': [
                                        'None', 'TransferItem', 'WorldEvent',
                                        'Train', 'Reference', 'Empty'
                                    ]
                                }
                            },
                            'Completion': {
                                'minRequestedAmount': 2,
                                'maxRequestedAmount': 10,
                                'minRequestedBulletAmount': 20,
                                'maxRequestedBulletAmount': 60,
                                'useWhitelist': True,
                                'useBlacklist': False,
                            },
                            'Elimination': {
                                'targets':
                                None,  #__REPLACEME__
                                'bodyPartProb':
                                0.4,
                                'bodyParts':
                                None,  #__REPLACEME__
                                'specificLocationProb':
                                0.25,
                                'distLocationBlacklist': [
                                    'laboratory', 'factory4_day',
                                    'factory4_night'
                                ],
                                'distProb':
                                0.25,
                                'maxDist':
                                200,
                                'minDist':
                                20,
                                'maxKills':
                                15,
                                'minKills':
                                5
                            }
                        }
                    }
                ]

        class ragfairconfig:
            sell = None
            traders = None
            dynamic = None

            @staticmethod
            def init():
                ragfairconfig.sell = {
                    'fees': True,
                    'chance': {
                        'base': 50,
                        'overprices': 0.5,
                        'underpriced': 2
                    },
                    'time': {
                        'base': 15,
                        'min': 5,
                        'max': 15
                    },
                    'reputation': {
                        'gain': 0.0000002,
                        'loss': 0.0000002
                    }
                }
                ragfairconfig.traders = {
                    '54cb50c76803fa8b248b4571': True,
                    '54cb57776803fa99248b456e': True,
                    '579dc571d53a0658a154fbec': False,
                    '58330581ace78e27b8b10cee': True,
                    '5935c25fb3acc3127c3d8cd9': True,
                    '5a7c2eca46aef81a7ca2145d': True,
                    '5ac3b934156ae10c4430e83c': True,
                    '5c0647fdd443bc2504c2d371': True,
                    'ragfair': False
                }
                ragfairconfig.dynamic = {
                    'expiredOfferThreshold':
                    1500,
                    'offerItemCount': {
                        'min': 7,
                        'max': 15
                    },
                    'price': {
                        'min': 0.8,
                        'max': 1.2
                    },
                    'endTimeSeconds': {
                        'min': 180,
                        'max': 1800
                    },
                    'condition': {
                        'conditionChance': 0.2,
                        'min': 0.6,
                        'max': 1
                    },
                    'stackablePercent': {
                        'min': 10,
                        'max': 500
                    },
                    'nonStackableCount': {
                        'min': 1,
                        'max': 10
                    },
                    'rating': {
                        'min': 0.1,
                        'max': 0.95
                    },
                    'currencies': {
                        '5449016a4bdc2d6f028b456f': 75,
                        '5696686a4bdc2da3298b456a': 23,
                        '569668774bdc2da2298b4568': 2
                    },
                    'showAsSingleStack': [
                        itemhelper.BASECLASS()['Weapon'],
                        itemhelper.BASECLASS()['Armor'],
                        itemhelper.BASECLASS()['SimpleContainer'],
                        itemhelper.BASECLASS()['Backpack'],
                        itemhelper.BASECLASS()['MobContainer'],
                        itemhelper.BASECLASS()['Key'],
                        itemhelper.BASECLASS()['MedKit']
                    ],
                    'blacklist': {
                        'custom': [
                            '55d7217a4bdc2d86028b456d',
                            '5af99e9186f7747c447120b8',
                            '557596e64bdc2dc2118b4571',
                            '566abbb64bdc2d144c8b457d',
                            '5cdeb229d7f00c000e7ce174',
                            '5cffa483d7ad1a049e54ef1c',
                            '5996f6d686f77467977ba6cc',
                            '5996f6cb86f774678763a6ca',
                            '5943d9c186f7745a13413ac9',
                            '5996f6fc86f7745e585b4de3',
                            '5cde8864d7f00c0010373be1',
                            '5d2f2ab648f03550091993ca'
                        ],
                        'enableBsgList':
                        True,
                        'enableQuestList':
                        True
                    }
                }

        class repairconfig:
            priceMultiplier = None

            @staticmethod
            def init():
                repairconfig.priceMultiplier = 1

        class saveconfig:
            runInterval = None

            @staticmethod
            def init():
                saveconfig.runInterval = 1

        class traderconfig:
            updateTime = None
            fenceAssortSize = None
            fenceMaxPresetsCount = None
            fencePresetPriceMult = None
            minDurabilityForSale = None
            fenceItemIgnoreList = []

            @staticmethod
            def init():
                traderconfig.updateTime = 3600,
                traderconfig.fenceAssortSize = 100,
                traderconfig.fenceMaxPresetsCount = 5,
                traderconfig.fencePresetPriceMult = 2.5,
                traderconfig.minDurabilityForSale = 60,
                traderconfig.fenceItemIgnoreList = [
                    '58ac60eb86f77401897560ff', '59e8936686f77467ce798647',
                    '56e294cdd2720b603a8b4575', '5661632d4bdc2d903d8b456b',
                    '543be5e94bdc2df1348b4568', '543be6674bdc2df1348b4569',
                    '5448bf274bdc2dfc2f8b456a', '543be5664bdc2dd4348b4569',
                    '5447bedf4bdc2d87278b4568'
                ]

        class weatherconfig:
            acceleration = None
            weather = {}

            @staticmethod
            def init():
                weatherconfig.acceleration = 7,
                weatherconfig.weather = {
                    'clouds': {
                        'min': -1.5,
                        'max': 1.5
                    },
                    'windSpeed': {
                        'min': 0,
                        'max': 3
                    },
                    'windDirection': {
                        'min': 0,
                        'max': 3
                    },
                    'windGustiness': {
                        'min': 0,
                        'max': 1
                    },
                    'rain': {
                        'min': 1,
                        'max': 4
                    },
                    'rainIntensity': {
                        'min': 0.1,
                        'max': 1
                    },
                    'fog': {
                        'min': 0.001,
                        'max': 0.03
                    },
                    'temp': {
                        'min': 0,
                        'max': 16
                    },
                    'pressure': {
                        'min': 760,
                        'max': 764
                    }
                }

    class controllers:

        class botcontroller:

            @staticmethod
            def init():
                pass

        class customizationcontroller:

            @staticmethod
            def init():
                pass

        class dialoguecontroller:

            @staticmethod
            def init():
                pass

            @staticmethod
            def adddialoguemessage(dialogueid, message, ssid, items=[]):
                messageid = hashutil.generate()
                dialogues = saveserver.profiles[ssid]['dialogues']
                if not dialogueid in dialogues:
                    dialogue = {
                        '_id': dialogueid,
                        'messages': [],
                        'pinned': False,
                        'new': 0,
                        'attachmentsNew': 0
                    }
                else:
                    dialogue = dialogues[dialogueid]
                dialogue['new'] += 1
                hasrewards = len(items) > 0
                timestamp = timeutil.gettimestamp()
                rewards = {}
                if hasrewards:
                    rewards['stash'] = hashutil.generate()
                    rewards['data'] = []
                    items = itemhelper.replaceids(items)
                    for item in items:
                        if not 'slotId' in item or item['slotId'] == 'hideout':
                            item['parentId'] = rewards['stash']
                            item['slotId'] = 'main'
                        rewards['data'].append(item)
                        valid, template = itemhelper.getitem(item['_tpl'])
                        if 'StackSlots' in template['_props']:
                            stackslotitems = itemhelper.generatestackslotitems(template, item['_id'])
                            for stackslotitem in stackslotitems:
                                rewards['data'].append(stackslotitem)
                    dialogue['attachmentsNew'] += 1
                dialoguemessage = {
                    '_id': messageid,
                    'uid': dialogueid,
                    'type': message['type'],
                    'dt': timestamp,
                    'localDateTime': timestamp,
                    'templateId': message['templateId'],
                    'text': message['text'],
                    'hasRewards': hasrewards,
                    'rewardCollected': False,
                    'items': items,
                    'maxStorageTime': message['maxStorageTime']
                }
                if 'systemData' in message:
                    dialoguemessage['systemData'] = message['systemData']
                dialogue['messages'].append(dialoguemessage)
                if message['type'] == 4 and 'ragfair' in message:
                    offersoldmessage = notifiercontroller.createoffersoldnotification(dialoguemessage, message['ragfair'])
                    notifiercontroller.sendmessage(ssid, offersoldmessage)
                    dialoguemessage['type'] = 13
                notificationmessage = notifiercontroller.createnewmessagenotification(dialoguemessage)
                notifiercontroller.sendmessage(ssid, notificationmessage)

        class gamecontroller:

            @staticmethod
            def init():
                pass

        class handbookcontroller:
            lookup = {}

            @staticmethod
            def init():
                handbookcontroller.lookup = {
                    'items': {
                        'byId': {},
                        'byParent': {}
                    },
                    'categories': {
                        'byId': {},
                        'byParent': {}
                    }
                }
                for item in databaseserver.tables['templates']['handbook'][
                        'Items']:
                    handbookcontroller.lookup['items']['byId'][
                        item['Id']] = item['Price']
                    if not item['ParentId'] in handbookcontroller.lookup[
                            'items']['byParent']:
                        handbookcontroller.lookup['items']['byParent'][
                            item['ParentId']] = []
                    handbookcontroller.lookup['items']['byParent'][
                        item['ParentId']].append(item['Id'])
                for category in databaseserver.tables['templates']['handbook'][
                        'Categories']:
                    if category['ParentId']:
                        handbookcontroller.lookup['categories']['byId'][
                            category['Id']] = category['ParentId']
                        if not category[
                                'ParentId'] in handbookcontroller.lookup[
                                    'categories']['byParent']:
                            handbookcontroller.lookup['categories'][
                                'byParent'][category['ParentId']] = []
                        handbookcontroller.lookup['categories']['byParent'][
                            category['ParentId']].append(category['Id'])
                    else:
                        handbookcontroller.lookup['categories']['byId'][
                            category['Id']] = None

            def gettemplateprice(id):
                if id in handbookcontroller.lookup['items']['byId']:
                    return handbookcontroller.lookup['items']['byId'][id]
                return 1

        class healthcontroller:

            @staticmethod
            def init(ssid):
                profile = saveserver.profiles[ssid]
                if not 'vitality' in profile:
                    profile['vitality'] = {
                        'health': {
                            'Hydration': 0,
                            'Energy': 0,
                            'Temperature': 0,
                            'Head': 0,
                            'Chest': 0,
                            'Stomach': 0,
                            'LeftArm': 0,
                            'RightArm': 0,
                            'LeftLeg': 0,
                            'RightLeg': 0
                        },
                        'effects': {
                            'Head': {},
                            'Chest': {},
                            'Stomach': {},
                            'LeftArm': {},
                            'RightArm': {},
                            'LeftLeg': {},
                            'RightLeg': {}
                        }
                    }

        class hideoutcontroller:

            @staticmethod
            def init():
                pass

        class inraidcontroller:

            @staticmethod
            def init(ssid):
                profile = saveserver.profiles[ssid]
                if not 'inraid' in profile:
                    profile['inraid'] = {
                        'location': 'none',
                        'character': 'none'
                    }

        class insurancecontroller:

            def init(ssid):
                profile = saveserver.profiles[ssid]
                if not 'insurance' in profile:
                    profile['insurance'] = []

        class inventorycontroller:

            @staticmethod
            def init():
                pass

        class launchercontroller:

            @staticmethod
            def init():
                pass

            @staticmethod
            def register(body):
                for ssid in saveserver.profiles:
                    if body['username'] == saveserver.profiles[ssid]['info'][
                            'username']:
                        return ''
                ssid = hashutil.generate()
                saveserver.profiles[ssid] = {
                    'info': {
                        'id': ssid,
                        'username': body['username'],
                        'password': body['password'],
                        'wipe': True,
                        'edition': body['edition']
                    }
                }
                saveserver.loadprofile(ssid)
                saveserver.saveprofile(ssid)
                return ssid

            @staticmethod
            def login(body):
                for ssid in saveserver.profiles:
                    profile = saveserver.profiles[ssid]
                    if body['username'] == profile['info']['username'] and body[
                            'password'] == profile['info']['password']:
                        return ssid
                return ''

            @staticmethod
            def find(ssid):
                if ssid in saveserver.profiles:
                    return saveserver.profiles[ssid]['info']
                return None

        class locationcontroller:

            @staticmethod
            def init():
                pass

        class matchcontroller:

            @staticmethod
            def init():
                pass

        class notecontroller:

            @staticmethod
            def init():
                pass

        class notifiercontroller:

            @staticmethod
            def init():
                pass

            @staticmethod
            def sendmessage(ssid, message):
                pass

            @staticmethod
            def createoffersoldnotification(dialoguemessage, ragfairdata):
                return {
                    'type': 'RagfairOfferSold',
                    'eventId': dialoguemessage['_id'],
                    'dialogId': dialoguemessage['uid'],
                    **ragfairdata
                }

            @staticmethod
            def createnewmessagenotification(dialoguemessage):
                return {
                    'type': 'new_message',
                    'eventId': dialoguemessage['_id'],
                    'dialogueId': dialoguemessage['uid'],
                    'message': dialoguemessage
                }

        class paymentcontroller:

            @staticmethod
            def init():
                pass

            @staticmethod
            def ismoneytpl(tpl):
                return tpl in [
                    '569668774bdc2da2298b4568', '5696686a4bdc2da3298b456a',
                    '5449016a4bdc2d6f028b456f'
                ]

            @staticmethod
            def fromrub(price, currency):
                return round(price /
                             handbookcontroller.gettemplateprice(currency))

        class playercontroller:

            @staticmethod
            def init():
                pass

        class presetbuildcontroller:

            @staticmethod
            def init():
                pass

        class presetcontroller:
            lookup = {}

            @staticmethod
            def init():
                for preset in list(databaseserver.tables['globals']
                                   ['ItemPresets'].values()):
                    tpl = preset['_items'][0]['_tpl']
                    if not tpl in presetcontroller.lookup:
                        presetcontroller.lookup[tpl] = []
                    presetcontroller.lookup[tpl].append(preset['_id'])

            @staticmethod
            def ispreset(id):
                return id in databaseserver.tables['globals']['ItemPresets']

            @staticmethod
            def haspreset(tpl):
                return tpl in presetcontroller.lookup

            @staticmethod
            def getpresets(tpl):
                presets = []
                if not presetcontroller.haspreset(tpl):
                    return presets
                idlist = presetcontroller.lookup[tpl]
                for id in idlist:
                    presets.append(
                        databaseserver.tables['globals']['ItemPresets'][id])
                return presets

        class profilecontroller:

            @staticmethod
            def init(ssid):
                profile = saveserver.profiles[ssid]
                if not 'characters' in profile:
                    profile['characters'] = {'pmc': {}, 'scav': {}}

            @staticmethod
            def getminiprofile(ssid):
                profile = profilecontroller.getpmcprofilebyssid(ssid)
                if not 'Info' in profile or not 'Level' in profile['Info']:
                    return {
                        'nickname': 'unknown',
                        'side': 'unknown',
                        'currlvl': 0,
                        'currexp': 0,
                        'prevexp': 0,
                        'nextlvl': 0,
                        'maxlvl': maxlvl
                    }
                maxlvl = profilecontroller.getmaxlevel()
                currlvl = profile['Info']['Level']
                nextlvl = profilecontroller.getexpbylevel(currlvl + 1)
                if currlvl == 0:
                    prevexp = 0 
                else:
                    prevexp = profilecontroller.getexpbylevel(currlvl)
                return {
                    'nickname': profile['Info']['Nickname'],
                    'side': profile['Info']['Side'],
                    'currlvl': currlvl,
                    'currexp': profile['Info']['Experience'],
                    'prevexp': prevexp,
                    'nextlvl': nextlvl,
                    'maxlvl': maxlvl
                }

            @staticmethod
            def getmaxlevel():
                return len(databaseserver.tables['globals']['config']['exp']
                           ['level']['exp_table']) - 1

            @staticmethod
            def getexpbylevel(level):
                maxlvl = profilecontroller.getmaxlevel()
                exp = 0
                if level > maxlvl:
                    level = maxlvl
                for i in range(0, level):
                    exp += databaseserver.tables['globals']['config']['exp'][
                        'level']['exp_table'][i]['exp']
                return exp

            @staticmethod
            def getpmcprofilebyssid(ssid):
                if not ssid in saveserver.profiles or not saveserver.profiles[
                        ssid]['characters']['pmc']:
                    return None
                return saveserver.profiles[ssid]['characters']['pmc']

            @staticmethod
            def getpmcprofilebypmcid(pmcid):
                for ssid in saveserver.profiles:
                    profile = saveserver.profiles[ssid]
                    if profile['characters']['pmc']['_id'] == pmcid:
                        return profile['characters']['pmc']
                return None

        class questcontroller:

            @staticmethod
            def init():
                pass

        class ragfaircontroller:

            @staticmethod
            def init():
                pass

            @staticmethod
            def returnitems(ssid, items):
                message = {
                    'text':
                    databaseserver['tables']['locales']['global']['ch']['mail']
                    ['5bdac06e86f774296f5a19c5'],
                    'type':
                    13,
                    'maxStorageTime':
                    questconfig.redeemTime * 3600
                }
                dialoguecontroller.adddialoguemessage(
                    '5ac3b934156ae10c4430e83c', message, ssid, items)

        class repaircontroller:

            @staticmethod
            def init():
                pass

        class repeatablequestcontroller:

            @staticmethod
            def init():
                pass

        class tradecontroller:

            @staticmethod
            def init():
                pass

        class tradercontroller:

            @staticmethod
            def init():
                pass

        class weathercontroller:

            @staticmethod
            def init():
                pass

        class wishlistcontroller:

            @staticmethod
            def init():
                pass

    class generators:

        class botgenerator:

            @staticmethod
            def init():
                pass

        class locationgenerator:

            @staticmethod
            def init():
                pass

        class pmclootgenerator:

            @staticmethod
            def init():
                pass

    class helpers:

        class containerhelper:

            @staticmethod
            def init():
                pass

        class durabilitylimitshelper:

            @staticmethod
            def init():
                pass

        class inventoryhelper:

            @staticmethod
            def init():
                pass

        class itemhelper:

            @staticmethod
            def init():
                pass

            @staticmethod
            def BASECLASS():
                return {
                    'Weapon': '5422acb9af1c889c16000029',
                    'Armor': '5448e54d4bdc2dcc718b4568',
                    'Vest': '5448e5284bdc2dcb718b4567',
                    'Backpack': '5448e53e4bdc2d60728b4567',
                    'Visors': '5448e5724bdc2ddf718b4568',
                    'Food': '5448e8d04bdc2ddf718b4569',
                    'Drink': '5448e8d64bdc2dce718b4568',
                    'BarterItem': '5448eb774bdc2d0a728b4567',
                    'Info': '5448ecbe4bdc2d60728b4568',
                    'MedKit': '5448f39d4bdc2d0a728b4568',
                    'Drugs': '5448f3a14bdc2d27728b4569',
                    'Stimulator': '5448f3a64bdc2d60728b456a',
                    'Medical': '5448f3ac4bdc2dce718b4569',
                    'MedicalSupplies': '57864c8c245977548867e7f1',
                    'Mod': '5448fe124bdc2da5018b4567',
                    'FunctionalMod': '550aa4154bdc2dd8348b456b',
                    'GearMod': '55802f3e4bdc2de7118b4584',
                    'Stock': '55818a594bdc2db9688b456a',
                    'Foregrip': '55818af64bdc2d5b648b4570',
                    'MasterMod': '55802f4a4bdc2ddb688b4569',
                    'Mount': '55818b224bdc2dde698b456f',
                    'Muzzle': '5448fe394bdc2d0d028b456c',
                    'Sights': '5448fe7a4bdc2d6f028b456b',
                    'Meds': '543be5664bdc2dd4348b4569',
                    'Money': '543be5dd4bdc2deb348b4569',
                    'Key': '543be5e94bdc2df1348b4568',
                    'KeyMechanical': '5c99f98d86f7745c314214b3',
                    'Keycard': '5c164d2286f774194c5e69fa',
                    'Equipment': '543be5f84bdc2dd4348b456a',
                    'ThrowWeap': '543be6564bdc2df4348b4568',
                    'FoodDrink': '543be6674bdc2df1348b4569',
                    'Pistol': '5447b5cf4bdc2d65278b4567',
                    'Smg': '5447b5e04bdc2d62278b4567',
                    'AssaultRifle': '5447b5f14bdc2d61278b4567',
                    'AssaultCarbine': '5447b5fc4bdc2d87278b4567',
                    'Shotgun': '5447b6094bdc2dc3278b4567',
                    'MarksmanRifle': '5447b6194bdc2d67278b4567',
                    'SniperRifle': '5447b6254bdc2dc3278b4568',
                    'MachineGun': '5447bed64bdc2d97278b4568',
                    'GrenadeLauncher': '5447bedf4bdc2d87278b4568',
                    'SpecialWeapon': '5447bee84bdc2dc3278b4569',
                    'SpecItem': '5447e0e74bdc2d3c308b4567',
                    'Knife': '5447e1d04bdc2dff2f8b4567',
                    'Ammo': '5485a8684bdc2da71d8b4567',
                    'AmmoBox': '543be5cb4bdc2deb348b4568',
                    'LootContainer': '566965d44bdc2d814c8b4571',
                    'MobContainer': '5448bf274bdc2dfc2f8b456a',
                    'SearchableItem': '566168634bdc2d144c8b456c',
                    'Stash': '566abbb64bdc2d144c8b457d',
                    'SortingTable': '6050cac987d3f925bf016837',
                    'LockableContainer': '5671435f4bdc2d96058b4569',
                    'SimpleContainer': '5795f317245977243854e041',
                    'Inventory': '55d720f24bdc2d88028b456d',
                    'StationaryContainer': '567583764bdc2d98058b456e',
                    'Pockets': '557596e64bdc2dc2118b4571',
                    'Armband': '5b3f15d486f77432d0509248',
                    'DogTagUsec': '59f32c3b86f77472a31742f0',
                    'DogTagBear': '59f32bb586f774757e1e8442',
                    'Jewelry': '57864a3d24597754843f8721',
                    'Electronics': '57864a66245977548f04a81f',
                    'BuildingMaterial': '57864ada245977548638de91',
                    'Tool': '57864bb7245977548b3b66c2',
                    'HouseholdGoods': '57864c322459775490116fbf',
                    'Lubricant': '57864e4c24597754843f8723',
                    'Battery': '57864ee62459775490116fc1',
                    'AssaultScope': '55818add4bdc2d5b648b456f',
                    'ReflexSight': '55818ad54bdc2ddc698b4569',
                    'TacticalCombo': '55818b164bdc2ddc698b456c',
                    'Magazine': '5448bc234bdc2d3c308b4569',
                    'LightLaser': '55818b0e4bdc2dde698b456e',
                    'Other': '590c745b86f7743cc433c5f2',
                    'Silencer': '550aa4cd4bdc2dd8348b456c',
                    'PortableRangeFinder': '61605ddea09d851a0a0c1bbc',
                    'Item': '54009119af1c881c07000029'
                }

            @staticmethod
            def MONEY():
                return {
                    'Roubles': '5449016a4bdc2d6f028b456f',
                    'Euros': '569668774bdc2da2298b4568',
                    'Dollars': '5696686a4bdc2da3298b456a'
                }

            @staticmethod
            def getitem(tpl):
                if tpl in databaseserver.tables['templates']['items']:
                    return True, databaseserver.tables['templates']['items'][
                        tpl]
                return False, {}

            @staticmethod
            def isvaliditem(tpl):
                valid, template = itemhelper.getitem(tpl)
                return valid

            @staticmethod
            def isquestitem(tpl):
                valid, template = itemhelper.getitem(tpl)
                if 'QuestItem' in template['_props']:
                    return template['_props']['QuestItem']
                return False

            @staticmethod
            def cansellonragfair(tpl):
                valid, template = itemhelper.getitem(tpl)
                if 'CanSellOnRagfair' in template['_props']:
                    return template['_props']['CanSellOnRagfair']
                return False

            @staticmethod
            def findandreturnchildrenbyassort(id, items):
                itemlist = []
                for item in items:
                    if item['parentId'] == id and len(
                            list(
                                filter(lambda i: i['_id'] == item['_id'],
                                       itemlist))) == 0:
                        itemlist.append(item)
                        itemlist = [
                            *itemlist,
                            *itemhelper.findandreturnchildrenbyassort(
                                item['_id'], items)
                        ]
                return itemlist

            @staticmethod
            def doesitemorparentsidmatch(tpl, tpllist):
                valid, template = itemhelper.getitem(tpl)
                if not valid:
                    return False
                if not '_parent' in template:
                    return False
                if template['_id'] in tpllist:
                    return True
                if template['_parent'] in tpllist:
                    return True
                return itemhelper.doesitemorparentsidmatch(
                    template['_parent'], tpllist)

            @staticmethod
            def getitemqualitymodifier(item):
                valid, template = itemhelper.getitem(item['_tpl'])
                result = 1
                if 'upd' in item:
                    if 'MedKit' in item['upd']:
                        result = item['upd']['MedKit'][
                            'HpResource'] / template['_props']['MaxHpResource']
                    if 'Repairable' in item['upd']:
                        result = item['upd']['Repairable']['Durability'] / item[
                            'upd']['Repairable']['MaxDurability']
                        if not 'armorClass' in template['_props']:
                            result = m.sqrt(result)
                    if result == 0:
                        result = 0.01
                return result

            @staticmethod
            def replaceids(items):
                return items

            @staticmethod
            def generatestackslotitems(item, parentid):
                stackslotitems = []
                for stackslot in item['_props']['StackSlots']:
                    slotid = stackslot['_name']
                    count = stackslot['_max_count']
                    ammotpl = stackslot['_props']['filters'][0]['Filter'][0]
                    stackslotitem = {
                        "_id": hashutil.generate(),
                        "_tpl": ammotpl,
                        "parentId": parentid,
                        "slotId": slotid,
                        "location": 0,
                        "upd": {
                            "StackObjectsCount": count
                        }
                    }
                    stackslotitems.append(stackslotitem)
                return stackslotitems

        class questhelper:

            @staticmethod
            def init():
                pass

        class traderhelper:

            @staticmethod
            def init():
                pass

        class utilityhelper:

            @staticmethod
            def init():
                pass

    class loaders:

        class bundleloader:

            @staticmethod
            def init():
                pass

        class modloader:
            moddir = 'user/mods/'
            infofile = 'modinfo.json'
            modclasses = {}

            @staticmethod
            def init():
                if filesystemutil.exists(modloader.moddir) and len(
                        filesystemutil.getdirs(modloader.moddir)) > 0:
                    logutil.info('加载MOD…')
                modloader.loadmods()
                modloader.executemods()

            @staticmethod
            def loadmods():
                if not filesystemutil.exists(modloader.moddir):
                    filesystemutil.makedir(modloader.moddir)
                mods = filesystemutil.getdirs(modloader.moddir)
                for mod in mods:
                    if modloader.validatemod(mod):
                        modinfo = modloader.getmodinfo(
                            modloader.getmodinfopath(mod))
                        imported = im.SourceFileLoader(
                            mod, ''.join([
                                modloader.getmodpath(mod), modinfo['modentry']
                            ])).load_module()
                        if not hasattr(imported, 'mod'):
                            logutil.error(' '.join(
                                ['MOD', mod, '加载失败：缺少入口类 mod']))
                            continue
                        if not hasattr(imported.mod, 'init'):
                            logutil.error(' '.join(
                                ['MOD', mod, '加载失败：缺少初始化方法 init']))
                            continue
                        modloader.modclasses[mod] = imported.mod

            @staticmethod
            def executemods():
                for _class in modloader.modclasses:
                    if isinstance(
                            modloader.modclasses[_class].__dict__['init'],
                            staticmethod):
                        modloader.modclasses[_class].init()
                    else:
                        modloader.modclasses[_class]().init()

            @staticmethod
            def validatemod(mod):
                infopath = modloader.getmodinfopath(mod)
                if not filesystemutil.exists(infopath):
                    logutil.error(' '.join(
                        ['MOD', mod, '加载失败：缺少MOD信息文件 ', modloader.infofile]))
                    return False
                infolist = [
                    'modname', 'modauthor', 'modentry', 'modversion',
                    'serverversion', 'license'
                ]
                modinfo = modloader.getmodinfo(infopath)
                for attr in infolist:
                    if not attr in modinfo:
                        logutil.error(' '.join([
                            'MOD', mod, '加载失败：在', modloader.infofile, '中缺少',
                            attr
                        ]))
                        return False
                entry = modinfo['modentry']
                if filesystemutil.getextsion(entry) != 'py':
                    logutil.error(' '.join(
                        ['MOD', mod, '加载失败：入口', entry, '非Py文件']))
                    return False
                if not filesystemutil.exists(''.join(
                    [modloader.getmodpath(mod), entry])):
                    logutil.error(' '.join(
                        ['MOD', mod, '加载失败：入口', entry, '文件不存在']))
                    return False
                if modinfo['serverversion'] != watermarkutil.version:
                    logutil.error(' '.join(['MOD', mod, '加载失败：与服务端版本不兼容']))
                    return False
                return True

            @staticmethod
            def getmodinfo(path):
                return jsonutil.parse(filesystemutil.readfile(path))

            @staticmethod
            def getmodinfopath(mod):
                return ''.join([modloader.getmodpath(mod), modloader.infofile])

            @staticmethod
            def getmodpath(mod):
                return ''.join([modloader.moddir, mod, '/'])

    class routers:

        class httprouter:
            onstatic = {}
            ondynamic = {}

            @staticmethod
            def init():
                logutil.info('加载路由地址…')
                httprouter.onstatic = staticroutes.getroutes()
                httprouter.ondynamic = dynamicroutes.getroutes()

            @staticmethod
            def getresponse(ssid, url, body, resp):
                result = ''
                if url.find('?retry=') != -1:
                    url = url.split('?retry=')[0]
                if url in httprouter.onstatic:
                    for callback in httprouter.onstatic[url]:
                        result = httprouter.onstatic[url][callback](ssid, url,
                                                                    body,
                                                                    result,
                                                                    resp)
                else:
                    for route in httprouter.ondynamic:
                        if url.find(route) != -1:
                            for callback in httprouter.ondynamic[route]:
                                result = httprouter.ondynamic[route][callback](
                                    ssid, url, body, result, resp)
                return result

        class imagerouter:
            onroute = {}

            @staticmethod
            def init():
                logutil.info('加载图片资源…')
                imagerouter.onroute = databaseutil.loadimages(''.join(
                    [databaseutil.dbdir, 'images/']))

            @staticmethod
            def sendimage(ssid, url, body, result, resp):
                path = filesystemutil.stripextension(url)
                if path in imagerouter.onroute:
                    result = imagerouter.onroute[path]
                    serverutil.wshttphandler.sendfile(ssid, url, body, result,
                                                      resp)

            @staticmethod
            def getimage(ssid, url, body, result, resp):
                return 'IMAGE'

        class itemeventrouter:
            onevent = {}
            result = {'warnings': [], 'profileChanges': {}}

            @staticmethod
            def init():
                logutil.info('加载事件钩子…')
                itemeventrouter.onevent = itemevents.getevents()

            @staticmethod
            def handleevents():
                pass

            @staticmethod
            def getresult(ssid):
                if not ssid in itemeventrouter.result['profileChanges']:
                    itemeventrouter.resetresult(ssid)
                return itemeventrouter.result

            @staticmethod
            def resetresult(ssid):
                profile = profilecontroller.getpmcprofilebyssid(ssid)
                itemeventrouter.result['warnings'] = []
                itemeventrouter.result['profileChanges'][ssid] = {
                    '_id': ssid,
                    'experience': 0,
                    'quests': [],
                    'ragFairOffers': [],
                    'builds': [],
                    'items': {
                        'new': [],
                        'change': [],
                        'del': []
                    },
                    'production': {},
                    'skills': {
                        'Common': jsonutil.clone(profile['Skills']['Common']),
                        'Mastering': [],
                        'Points': 0
                    },
                    'traderRelations': {}
                }

    class servers:

        class databaseserver:
            tables = {}

            @staticmethod
            def init():
                pass

        class httpserver:
            onrespond = {}
            wspinghandler = []
            buffers = {}
            mime = {
                'css': 'text/css',
                'bin': 'application/octet-stream',
                'html': 'text/html',
                'jpg': 'image/jpeg',
                'js': 'text/javascript',
                'json': 'application/json',
                'png': 'image/png',
                'svg': 'image/svg+xml',
                'txt': 'text/plain'
            }

            @staticmethod
            def init():
                logutil.info('启动服务器…')
                httpserver.onrespond = serverresponse.getresponses()
                hostandport = httpserver.gethostport()
                backendserver = serverutil.wshttpserver(
                    hostandport, serverutil.wshttphandler)
                backendserver.start()
                logutil.success(' '.join(['服务器已开启，监听端口', str(hostandport[1])]))

            @staticmethod
            def gethostport():
                host = databaseserver.tables['server']['ip']
                port = databaseserver.tables['server']['port']
                return (host, port)

            @staticmethod
            def getbackendurl():
                hostandport = httpserver.gethostport()
                return ''.join(
                    ['http://', hostandport[0], ':',
                     str(hostandport[1])])

        class ragfairserver:
            offers = []
            exipredoffers = []
            traders = {}
            categories = {}
            linkeditems = {}
            requireditems = {}
            staticprices = {}
            dynamicprices = {}

            @staticmethod
            def init():
                ragfairserver.buildlinkeditems()
                ragfairserver.generatestaticprices()
                ragfairserver.generatedynamicprices()
                ragfairserver.generatedynamicoffers()
                ragfairserver.addtraders()
                ragfairserver.update()

            @staticmethod
            def buildlinkeditems():
                for item in list(
                        databaseserver.tables['templates']['items'].values()):
                    ragfairserver.getlinkeditems(item['_id'])
                    slots = ragfairserver.getfilters(item, 'Slots')
                    chambers = ragfairserver.getfilters(item, 'Chambers')
                    cartridges = ragfairserver.getfilters(item, 'Cartridges')
                    ragfairserver.applylinkeditems(item, slots)
                    ragfairserver.applylinkeditems(item, chambers)
                    ragfairserver.applylinkeditems(item, cartridges)

            @staticmethod
            def getlinkeditems(id):
                if not id in ragfairserver.linkeditems:
                    ragfairserver.linkeditems[id] = []
                return ragfairserver.linkeditems[id]

            @staticmethod
            def applylinkeditems(item, items):
                for linkeditemid in items:
                    linkeditems = ragfairserver.getlinkeditems(linkeditemid)
                    if not item['_id'] in linkeditems:
                        linkeditems.append(item['_id'])

            @staticmethod
            def getfilters(item, slot):
                filters = []
                if not (slot in item['_props'] and item['_props'][slot]):
                    return filters
                for sub in item['_props'][slot]:
                    if not ('_props' in sub and 'filters' in sub['_props']):
                        continue
                    for filter in sub['_props']['filters']:
                        for f in filter['Filter']:
                            filters.append(f)
                return filters

            @staticmethod
            def generatestaticprices():
                for itemtpl in databaseserver.tables['templates']['items']:
                    ragfairserver.staticprices[itemtpl] = round(
                        handbookcontroller.gettemplateprice(itemtpl))

            @staticmethod
            def generatedynamicprices():
                dynamicprices = {
                    **ragfairserver.staticprices,
                    **databaseserver.tables['templates']['prices']
                }
                for itemtpl in dynamicprices:
                    if not dynamicprices[itemtpl]:
                        ragfairserver.dynamicprices[itemtpl] = 1
                    else:
                        ragfairserver.dynamicprices[itemtpl] = dynamicprices[
                            itemtpl]

            @staticmethod
            def generatedynamicoffers(expiredoffers=None):
                assort = jsonutil.clone(
                    databaseserver.tables['traders']['ragfair']['assort'])
                if expiredoffers:
                    assortitems = expiredoffers
                else:
                    assortitems = list(
                        filter(lambda item: item['slotId'] == 'hideout',
                               assort['items']))
                itemindex = 0
                for item in assortitems:
                    itemid = item['_id']
                    itemtpl = item['_tpl']
                    if not itemhelper.isvaliditem(itemtpl):
                        continue
                    if ragfairserver.isitemindynamicblacklist(itemtpl):
                        continue
                    if ragfairconfig.dynamic['blacklist'][
                            'enableQuestList'] and itemhelper.isquestitem(
                                itemtpl):
                        continue
                    if ragfairconfig.dynamic['blacklist'][
                            'enableBsgList'] and not itemhelper.cansellonragfair(
                                itemtpl):
                        continue
                    ispreset = presetcontroller.ispreset(itemid)
                    if ispreset:
                        items = ragfairserver.getpresetitems(item)
                    else:
                        items = [
                            *[item], *itemhelper.findandreturnchildrenbyassort(
                                itemid, assort['items'])
                        ]
                    if expiredoffers:
                        itemcount = 1
                    else:
                        itemcount = round(
                            randomutil.getint(
                                ragfairconfig.dynamic['offerItemCount']['min'],
                                ragfairconfig.dynamic['offerItemCount']
                                ['max']))
                    for index in range(0, itemcount):
                        items[0]['upd'][
                            'StackObjectsCount'] = ragfairserver.calculatedynamicstackcount(
                                items[0]['_tpl'], ispreset)
                        userid = hashutil.generate()
                        valid, template = itemhelper.getitem(itemtpl)
                        items = ragfairserver.getitemcondition(
                            userid, items, template)
                        barterscheme = ragfairserver.getofferrequirements(
                            items)
                        price = ragfairserver.getbarterprice(barterscheme)
                        ragfairserver.createoffer(
                            userid, timeutil.gettimestamp(), items,
                            barterscheme,
                            assort['loyal_level_items'][item['_id']], price,
                            ispreset)
                    if expiredoffers:
                        del expiredoffers[itemindex]
                    itemindex += 1

            @staticmethod
            def isitemindynamicblacklist(tpl):
                return tpl in ragfairconfig.dynamic['blacklist']['custom']

            @staticmethod
            def getpresetitems(item):
                preset = jsonutil.clone(databaseserver.tables['globals']
                                        ['ItemPresets'][item['_id']]['_items'])
                return ragfairserver.reparentpresets(item, preset)

            @staticmethod
            def getpresetitemsbytpl(item):
                presets = []
                for itemid in databaseserver.tables['globals']['ItemPresets']:
                    if databaseserver.tables['globals']['ItemPresets'][itemid][
                            '_items'][0]['_tpl'] == item['_tpl']:
                        preset = jsonutil.clone(
                            databaseserver.tables['globals']['ItemPresets'][
                                item['_id']]['_items'])
                        presets.push(
                            ragfairserver.reparentpresets(item, preset))
                return presets

            @staticmethod
            def reparentpresets(item, preset):
                rootitemid = preset[0]['_id']
                iddict = {}
                iddict[rootitemid] = item['_id']
                for mod in preset:
                    if not mod['_id'] in iddict:
                        iddict[mod['_id']] = hashutil.generate()
                    if 'parentId' in mod and not mod['parentId'] in iddict:
                        iddict[mod['parentId']] = hashutil.generate()
                    mod['_id'] = iddict[mod['_id']]
                    if 'parentId' in mod:
                        mod['parentId'] = iddict[mod['parentId']]
                preset[0] = item
                return preset

            @staticmethod
            def calculatedynamicstackcount(tpl, ispreset):
                valid, template = itemhelper.getitem(tpl)
                if not valid:
                    raise ' '.join(['未找到TPL为', tpl, '的物品，无法为其生成随机数量'])
                if ispreset or itemhelper.doesitemorparentsidmatch(
                        template['_id'],
                        ragfairconfig.dynamic['showAsSingleStack']):
                    return 1
                if not 'StackMaxSize' in template['_props'] or template[
                        '_props']['StackMaxSize'] == 1:
                    return round(
                        randomutil.getint(
                            ragfairconfig.dynamic['nonStackableCount']['min'],
                            ragfairconfig.dynamic['nonStackableCount']['max']))
                stackPercent = round(
                    randomutil.getint(
                        ragfairconfig.dynamic['stackablePercent']['min'],
                        ragfairconfig.dynamic['stackablePercent']['max']))
                return round(
                    (template['_props']['StackMaxSize'] / 100) * stackPercent)

            @staticmethod
            def getitemcondition(userid, items, template):
                item = ragfairserver.addmissingcondition(items[0])
                if not ragfairserver.isplayer(
                        userid) and not ragfairserver.istrader(userid):
                    if randomutil.getint(0, 99) < ragfairconfig.dynamic[
                            'condition']['conditionChance'] * 100:
                        multiplier = randomutil.getfloat(
                            ragfairconfig.dynamic['condition']['min'],
                            ragfairconfig.dynamic['condition']['max'])
                        if 'Repairable' in item['upd']:
                            if 'armorClass' in template['_props'] and template[
                                    '_props']['armorClass'] != '0':
                                item['upd']['Repairable']['Durability'] = round(
                                    item['upd']['Repairable']['Durability'] *
                                    multiplier) or 1
                            if 'armorClass':
                                item['upd']['Repairable']['Durability'] = round(
                                    item['upd']['Repairable']['Durability'] *
                                    multiplier) or 1
                        if 'MedKit' in item['upd']:
                            item['upd']['MedKit']['HpResource'] = round(
                                item['upd']['MedKit']['HpResource'] *
                                multiplier) or 1
                items[0] = item
                return items

            @staticmethod
            def addmissingcondition(item):
                valid, template = itemhelper.getitem(item['_tpl'])
                if 'Durability' in template[
                        '_props'] and template['_props']['Durability'] > 0:
                    item['upd']['Repairable'] = {
                        'Durability': template['_props']['Durability'],
                        'MaxDurability': template['_props']['Durability']
                    }
                if 'MaxHpResource' in template[
                        '_props'] and template['_props']['MaxHpResource'] > 0:
                    item['upd']['MedKit'] = {
                        'HpResource': template['_props']['MaxHpResource']
                    }
                return item

            @staticmethod
            def isplayer(userid):
                if profilecontroller.getpmcprofilebyssid(userid) != None:
                    return True
                return False

            @staticmethod
            def istrader(userid):
                return userid in databaseserver.tables['traders']

            @staticmethod
            def getofferrequirements(items):
                currency = ragfairserver.getdynamicoffercurrency()
                price = ragfairserver.getdynamicofferprice(items, currency)
                return [{'count': price, '_tpl': currency}]

            @staticmethod
            def getdynamicoffercurrency():
                currencies = ragfairconfig.dynamic['currencies']
                bias = []
                for currency in currencies:
                    for i in range(0, currencies[currency]):
                        bias.append(currency)
                return bias[m.floor(ra.random() * len(bias))]

            @staticmethod
            def getdynamicofferprice(items, currency):
                price = 0
                endloop = False
                for item in items:
                    if not item[
                            '_tpl'] in ragfairserver.dynamicprices or ragfairserver.dynamicprices[
                                item['_tpl']] == 1:
                        itemdynamicprice = handbookcontroller.gettemplateprice(
                            item['_tpl'])
                    else:
                        itemdynamicprice = ragfairserver.dynamicprices[
                            item['_tpl']]
                    valid, template = itemhelper.getitem(item['_tpl'])
                    if presetcontroller.ispreset(
                            item['_id']
                    ) and 'weapFireType' in template['_props']:
                        itemdynamicprice = ragfairserver.getweaponpresetprice(
                            item, items, itemdynamicprice)
                        endloop = True
                    if currency != itemhelper.MONEY()['Roubles']:
                        itemdynamicprice = paymentcontroller.fromrub(
                            itemdynamicprice, currency)
                    itemqualitymodifier = itemhelper.getitemqualitymodifier(
                        item)
                    price += itemdynamicprice * itemqualitymodifier
                    if endloop:
                        break
                price = round(
                    price *
                    randomutil.getfloat(ragfairconfig.dynamic['price']['min'],
                                        ragfairconfig.dynamic['price']['max']))
                if price < 1:
                    price = 1
                return price

            @staticmethod
            def getweaponpresetprice(item, items, price):
                presets = presetcontroller.getpresets(item['_tpl'])
                if len(presets) == 0:
                    logutil.warning(' '.join(['物品', item['_tpl'], '没有预设']))
                    return price
                defaultpreset = list(
                    filter(lambda i: '_encyclopedia' in i, presets))
                if len(defaultpreset) == 0:
                    defaultpreset = presets[0]
                else:
                    defaultpreset = defaultpreset[0]
                neworreplacedmods = list(
                    filter(
                        lambda i: len(
                            list(
                                filter(lambda j: i['_tpl'] == j['_tpl'],
                                       defaultpreset['_items']))) == 0, items))
                extramodsprice = 0
                for mod in neworreplacedmods:
                    extramodsprice += ragfairserver.dynamicprices[mod['_tpl']]
                if len(neworreplacedmods) >= 1:
                    replacedmods = list(
                        filter(
                            lambda i: len(
                                list(
                                    filter(lambda j: i['_tpl'] == j['_tpl'],
                                           defaultpreset['_items']))) == 0,
                            neworreplacedmods))
                    replacedmodsprice = 0
                    for mod in replacedmods:
                        replacedmodsprice += ragfairserver.dynamicprices[
                            mod['_tpl']]
                    extramodsprice -= replacedmodsprice
                return price + extramodsprice

            @staticmethod
            def getbarterprice(barterscheme):
                price = 0
                for item in barterscheme:
                    price += ragfairserver.staticprices[
                        item['_tpl']] * item['count']
                return round(price)

            @staticmethod
            def createoffer(userid,
                            timestamp,
                            items,
                            barterscheme,
                            loyallevel,
                            price,
                            sellinonepiece=False):
                offer = {
                    '_id': ragfairserver.getofferid(userid, items),
                    'intId': 0,
                    'user': {
                        'id': ragfairserver.gettraderid(userid),
                        'memberType': ragfairserver.getmembertype(userid),
                        'nickname': ragfairserver.getnickname(userid),
                        'rating': ragfairserver.getrating(userid),
                        'isRatingGrowing':
                        ragfairserver.getratinggrowing(userid),
                        'avatar': ragfairserver.gettraderavatar(userid)
                    },
                    'root': items[0]['_id'],
                    'items': jsonutil.clone(items),
                    'requirements': barterscheme,
                    'requirementsCost': price,
                    'itemsCost': price,
                    'summaryCost': price,
                    'startTime': timestamp,
                    'endTime':
                    ragfairserver.getofferendtime(userid, timestamp),
                    'loyaltyLevel': loyallevel,
                    'sellInOnePiece': sellinonepiece,
                    'priority': False
                }
                ragfairserver.offers.append(offer)
                return offer

            @staticmethod
            def getofferid(userid, items):
                if ragfairserver.istrader(userid):
                    return items[0]['_id']
                return hashutil.generate()

            @staticmethod
            def gettraderid(userid):
                if ragfairserver.isplayer(userid):
                    return profilecontroller.getpmcprofilebyssid(userid)['_id']
                return userid

            @staticmethod
            def getmembertype(userid):
                if ragfairserver.isplayer(userid):
                    return profilecontroller.getpmcprofilebyssid(
                        userid)['Info']['AccountType']
                if ragfairserver.istrader(userid):
                    return 4
                return 0

            @staticmethod
            def getnickname(userid):
                if ragfairserver.isplayer(userid):
                    return profilecontroller.getpmcprofilebyssid(
                        userid)['Info']['Nickname']
                if ragfairserver.istrader(userid):
                    return databaseserver.tables['traders'][userid]['base'][
                        'nickname']
                if randomutil.getbool():
                    side = 'usec'
                else:
                    side = 'bear'
                while True:
                    name = randomutil.getlistelement(
                        databaseserver.tables['bots']['types'][side]
                        ['firstName'])
                    if len(name) <= 15:
                        break
                return name

            @staticmethod
            def getrating(userid):
                if ragfairserver.isplayer(userid):
                    return profilecontroller.getpmcprofilebyssid(
                        userid)['RagfairInfo']['rating']
                if ragfairserver.istrader(userid):
                    return 1
                return randomutil.getfloat(
                    ragfairconfig.dynamic['rating']['min'],
                    ragfairconfig.dynamic['rating']['max'])

            @staticmethod
            def getratinggrowing(userid):
                if ragfairserver.isplayer(userid):
                    return profilecontroller.getpmcprofilebyssid(
                        userid)['RagfairInfo']['isRatingGrowing']
                if ragfairserver.istrader(userid):
                    return True
                return randomutil.getbool()

            @staticmethod
            def gettraderavatar(userid):
                if ragfairserver.istrader(userid):
                    return databaseserver.tables['traders'][userid]['base'][
                        'avatar']
                return databaseserver.tables['traders']['ragfair']['base'][
                    'avatar']

            @staticmethod
            def getofferendtime(userid, timestamp):
                if ragfairserver.isplayer(userid):
                    return timestamp + round(12 * 3600)
                if ragfairserver.istrader(userid):
                    return databaseserver.tables['traders'][userid]['base'][
                        'nextResupply']
                return round(timestamp + randomutil.getint(
                    ragfairconfig.dynamic['endTimeSeconds']['min'],
                    ragfairconfig.dynamic['endTimeSeconds']['max']))

            @staticmethod
            def addtraders():
                for trader in databaseserver.tables['traders']:
                    if not trader in ragfairconfig.traders:
                        ragfairserver.traders[trader] = False
                    else:
                        ragfairserver.traders[trader] = ragfairconfig.traders[
                            trader]

            @staticmethod
            def update():
                time = timeutil.gettimestamp()
                offerindex = 0
                for offer in ragfairserver.offers:
                    if ragfairserver.isexpired(offer, time):
                        if ragfairserver.istrader(offer['user']['id']):
                            ragfairserver.traders[offer['user']['id']] = True
                        elif not ragfairserver.isplayer(
                                re.sub(r'^pmc', '', offer['user']['id'])):
                            ragfairserver.exipredoffers.append(
                                offer['items'][0])
                        if ragfairserver.isplayer(
                                re.sub(r'^pmc', '', offer['user']['id'])):
                            ragfairserver.returnplayeroffer(offer)
                        del ragfairserver.offers[offerindex]
                        offerindex += 1
                for trader in ragfairserver.traders:
                    if ragfairserver.traders[trader]:
                        ragfairserver.generatetraderoffers(trader)
                        ragfairserver.traders[trader] = False
                if len(ragfairserver.exipredoffers
                       ) >= ragfairconfig.dynamic['expiredOfferThreshold']:
                    ragfairserver.generatedynamicprices()
                    ragfairserver.generatedynamicoffers(
                        ragfairserver.exipredoffers)
                for offer in ragfairserver.offers:
                    ragfairserver.categories[offer['items'][0]['_tpl']] = 1
                ragfairserver.buildrequireditemtable()

            @staticmethod
            def buildrequireditemtable():
                for offer in ragfairserver.offers:
                    for requirement in offer['requirements']:
                        requireditemtpl = requirement['_tpl']
                        if paymentcontroller.ismoneytpl(requireditemtpl):
                            continue
                        ragfairserver.getrequireditems(requireditemtpl)
                        ragfairserver.applyrequireditems(
                            requireditemtpl, offer)

            @staticmethod
            def getrequireditems(tpl):
                if not tpl in ragfairserver.requireditems:
                    ragfairserver.requireditems[tpl] = []
                return ragfairserver.requireditems[tpl]

            @staticmethod
            def applyrequireditems(tpl, offer):
                requireditems = ragfairserver.getrequireditems(tpl)
                if not offer in requireditems:
                    requireditems.append(offer)

            @staticmethod
            def isexpired(offer, time):
                return offer['endTime'] < time or offer['items'][0]['upd'][
                    'StackObjectsCount'] < 1

            @staticmethod
            def generatetraderoffers(trader):
                ragfairserver.offers = list(
                    filter(lambda o: o['user']['id'] != trader,
                           ragfairserver.offers))
                time = timeutil.gettimestamp()
                assort = databaseserver.tables['traders'][trader]['assort']
                for item in assort['items']:
                    if item['slotId'] != 'hideout':
                        continue
                    ispreset = presetcontroller.ispreset(item['_id'])
                    if ispreset:
                        items = ragfairserver.getpresetitems(item)
                    else:
                        items = [
                            *[item], *itemhelper.findandreturnchildrenbyassort(
                                item['_id'], assort['items'])
                        ]
                    barterscheme = assort['barter_scheme'][item['_id']][0]
                    loyallevel = assort['loyal_level_items'][item['_id']]
                    price = ragfairserver.getbarterprice(barterscheme)
                    ragfairserver.createoffer(trader, time, items,
                                              barterscheme, loyallevel, price)

            @staticmethod
            def addplayeroffers():
                pass

            @staticmethod
            def returnplayeroffer(offer):
                offercount = len(profile['RagfairInfo']['offers'])
                if offercount == 0:
                    return
                profile = profilecontroller.getpmcprofilebypmcid(
                    offer['user']['id'])
                for index in range(0, offercount + 1):
                    if index == offercount:
                        logutil.warning(' '.join(
                            ['未找到ID为', offer['_id'], '的报价']))
                        return httputil.appenderror(
                            itemeventrouter.getresult(profile['aid']), '报价不存在',
                            '错误')
                    if profile['RagfairInfo']['offers'][index]['_id'] == offer[
                            '_id']:
                        break
                if offer['items'][0]['upd']['StackObjectsCount'] > offer[
                        'items'][0]['upd']['OriginalStackObjectsCount']:
                    offer['items'][0]['upd']['StackObjectsCount'] = offer[
                        'items'][0]['upd']['OriginalStackObjectsCount']
                del offer['items'][0]['upd']['OriginalStackObjectsCount']
                ragfaircontroller.returnitems(profile['aid'], offer['items'])
                del profile['RagfairInfo']['offers'][index]
                offercount = len(ragfairserver.offers)
                for index in range(0, offercount + 1):
                    if index == offercount:
                        logutil.warning(' '.join(
                            ['未找到ID为', offer['_id'], '的报价']))
                    if ragfairserver.offers[index]['_id'] == offer['_id']:
                        break
                del ragfairserver.offers[index]
                return itemeventrouter.getresult(profile['aid'])

        class saveserver:
            profilesdir = 'user/profiles/'
            initfunctions = {}
            profiles = {}
            profilemd5 = {}

            @staticmethod
            def init():
                saveserver.initfunctions = saveinitfunctions.getfunctions()
                if not filesystemutil.exists(saveserver.profilesdir):
                    filesystemutil.makedir(saveserver.profilesdir)
                profiles = [
                    file
                    for file in filesystemutil.getfiles(saveserver.profilesdir)
                    if filesystemutil.getextsion(file) == 'json'
                ]
                for profile in profiles:
                    saveserver.loadprofile(filesystemutil.getfilename(profile))
                ragfairserver.addplayeroffers()

            @staticmethod
            def save():
                for ssid in saveserver.profiles:
                    saveserver.saveprofile(ssid)
                return True

            @staticmethod
            def loadprofile(ssid):
                profile = ''.join([saveserver.profilesdir, ssid, '.json'])
                if filesystemutil.exists(profile):
                    saveserver.profiles[ssid] = jsonutil.parse(
                        filesystemutil.readfile(profile))
                for function in saveserver.initfunctions:
                    saveserver.initfunctions[function](ssid)

            @staticmethod
            def saveprofile(ssid):
                profile = ''.join([saveserver.profilesdir, ssid, '.json'])
                jsonprofile = jsonutil.unparse(saveserver.profiles[ssid], True)
                jsonprofilemd5 = hashutil.generatemd5(jsonprofile)
                if not ssid in saveserver.profilemd5 or saveserver.profilemd5[
                        ssid] != jsonprofilemd5:
                    saveserver.profilemd5[ssid] = jsonprofilemd5
                    filesystemutil.writefile(profile, jsonprofile)

    class utils:

        class initializer:
            initfunctions = {}
            updfunctions = {}
            updlastruntime = {}

            @staticmethod
            def init():
                initializer.initfunctions = initializefunctions.getfunctions()
                initializer.updfunctions = updatefunctions.getfunctions()
                logutil.info('初始化服务端…')
                for function in initializer.initfunctions:
                    initializer.initfunctions[function]()
                taskutil.setloop(func=initializer.update)

            @staticmethod
            def update():
                for function in initializer.updfunctions:
                    if not function in initializer.updlastruntime:
                        initializer.updlastruntime[
                            function] = timeutil.gettimestamp()
                    timesincelastrun = timeutil.gettimestamp(
                    ) - initializer.updlastruntime[function]
                    success = initializer.updfunctions[function](
                        timesincelastrun)
                    if success:
                        initializer.updlastruntime[
                            function] = timeutil.gettimestamp()
                    if success == None and timesincelastrun % 300 == 0:
                        logutil.error(' '.join(['定时事件', function, '执行失败']))

        class databaseutil:
            if len(sys.argv) == 1:
                dbdir = 'Aki_Data/Server/'
            elif sys.argv[1] == 'test-debug':
                dbdir = 'assets/'

            @staticmethod
            def init():
                logutil.info('加载数据文件…')
                databaseserver.tables = databaseutil.loadjsons(''.join(
                    [databaseutil.dbdir, 'database/']))

            @staticmethod
            def loadjsons(path):
                result = {}
                files = filesystemutil.getfiles(path)
                dirs = filesystemutil.getdirs(path)
                for file in files:
                    if filesystemutil.getextsion(file) == 'json':
                        result[filesystemutil.getfilename(
                            file)] = jsonutil.parse(
                                filesystemutil.readfile(''.join([path, file])))
                for dir in dirs:
                    result[dir] = databaseutil.loadjsons(''.join(
                        [path, dir, '/']))
                return result

            @staticmethod
            def loadimages(path):
                result = {}
                dirs = filesystemutil.getdirs(path)
                routes = ('/files/CONTENT/banners/', '/files/handbook/',
                          '/files/Hideout/', '/files/launcher/',
                          '/files/quest/icon/', '/files/trader/avatar/')
                for i in range(0, len(dirs) - 1):
                    dirpath = ''.join([path, dirs[i]])
                    files = filesystemutil.getfiles(''.join([dirpath, '/']))
                    for file in files:
                        result[''.join([
                            routes[i],
                            filesystemutil.stripextension(file)
                        ])] = '/'.join([dirpath, file])
                result['/favicon.ico'] = ''.join([path, 'icon.ico'])
                return result

        class filesystemutil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def exists(path):
                return os.path.exists(path)

            @staticmethod
            def makedir(path):
                os.makedirs(path)

            @staticmethod
            def readfile(path):
                with open(path, 'r', encoding='utf-8') as file:
                    read = file.read()
                return read

            @staticmethod
            def writefile(path, data, append=False):
                if not filesystemutil.exists(path):
                    with open(path, 'w') as file:
                        file.write('')
                if append:
                    with open(path, 'a', encoding='utf-8') as file:
                        file.write(data)
                else:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(data)

            @staticmethod
            def getfiles(path):
                return [
                    file for file in os.listdir(path)
                    if os.path.isfile(''.join([path, file]))
                ]

            @staticmethod
            def getdirs(path):
                return [
                    dir for dir in os.listdir(path)
                    if os.path.isdir(''.join([path, dir]))
                ]

            @staticmethod
            def getfiledir(path):
                return ''.join([os.path.dirname(path), '/'])

            @staticmethod
            def getfilename(path):
                return os.path.splitext(os.path.basename(path))[0]

            @staticmethod
            def getextsion(path):
                return os.path.splitext(path)[1][1:]

            @staticmethod
            def stripextension(path):
                return os.path.splitext(path)[0]

        class hashutil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def generate():
                randomtime = ra.uniform(0, 1) * timeutil.gettimestamp()
                return hl.sha1(
                    str(randomtime).encode('utf-8')).hexdigest()[:24]

            @staticmethod
            def generatemd5(data):
                return hl.md5(data.encode('utf-8')).hexdigest()

        class httputil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getclearedstring(str):
                return str.replace('\b', '').replace('\f', '').replace(
                    '\n', '').replace('\r', '').replace('\t',
                                                        '').replace('\\', '')

            @staticmethod
            def getnobody(data):
                return httputil.getclearedstring(jsonutil.unparse(data))

            @staticmethod
            def getclearedbody(data, err=0, msg=None):
                return httputil.getclearedstring(
                    httputil.getunclearedbody(data, err, msg))

            @staticmethod
            def getunclearedbody(data, err=0, msg=None):
                return jsonutil.unparse({
                    'err': err,
                    'errmsg': msg,
                    'data': data
                })

            @staticmethod
            def getemptyresponse():
                return httputil.getclearedbody('', 0, '')

            @staticmethod
            def getnoneresponse():
                return httputil.getclearedbody(None)

            @staticmethod
            def getemptylistresponse():
                return httputil.getclearedbody([])

            @staticmethod
            def appenderror(result,
                            msg='An unknown error occurred',
                            title='Error'):
                result['warnings'] = [{
                    'index': 0,
                    'err': title,
                    'errmsg': msg
                }]
                return result

        class jsonutil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def unparse(data, beautify=False):
                if beautify:
                    return js.dumps(data,
                                    option=js.OPT_INDENT_2).decode('utf-8')
                return js.dumps(data).decode('utf-8')

            @staticmethod
            def parse(data):
                return js.loads(data)

            @staticmethod
            def clone(data):
                return cp.deepcopy(data)

        class logutil:
            logfile = 'user/logs/server.log'
            frontcolor = {
                'black': '\x1b[30m',
                'red': '\x1b[31m',
                'green': '\x1b[32m',
                'yellow': '\x1b[33m',
                'blue': '\x1b[34m',
                'magenta': '\x1b[35m',
                'cyan': '\x1b[36m',
                'white': '\x1b[37m'
            }
            backcolor = {
                'black': '\x1b[40m',
                'red': '\x1b[41m',
                'green': '\x1b[42m',
                'yellow': '\x1b[43m',
                'blue': '\x1b[44m',
                'magenta': '\x1b[45m',
                'cyan': '\x1b[46m',
                'white': '\x1b[47m'
            }

            @staticmethod
            def init():
                if not filesystemutil.exists(
                        filesystemutil.getfiledir(logutil.logfile)):
                    filesystemutil.makedir(
                        filesystemutil.getfiledir(logutil.logfile))
                filesystemutil.writefile(logutil.logfile, '')
                sys.excepthook = logutil.handle

            @staticmethod
            def handle(type, value, trace):
                exception = tb.format_exception(type, value, trace)
                for err in exception:
                    logutil.error(err[0:-1])
                sys.exit(1)

            @staticmethod
            def write(data):
                filesystemutil.writefile(logutil.logfile,
                                         ''.join([data, '\n']), True)

            @staticmethod
            def log(data, front='', back=''):
                frontcolor = logutil.frontcolor[
                    front] if front in logutil.frontcolor else ''
                backcolor = logutil.backcolor[
                    back] if back in logutil.backcolor else ''
                colors = ''.join([frontcolor, backcolor])
                if colors:
                    print(''.join([colors, data, '\x1b[0m']))
                else:
                    print(data)
                logutil.write(data)

            @staticmethod
            def success(data):
                logutil.log(' '.join(['[成功]', str(data)]), 'white', 'green')

            @staticmethod
            def info(data):
                logutil.log(' '.join(['[信息]', str(data)]), 'cyan', '')

            @staticmethod
            def error(data):
                logutil.log(' '.join(['[错误]', str(data)]), 'white', 'red')

            @staticmethod
            def warning(data):
                logutil.log(' '.join(['[警告]', str(data)]), 'black', 'yellow')

        class randomutil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def getint(min, max):
                return ra.randint(min, max)

            @staticmethod
            def getfloat(min, max):
                return ra.uniform(min, max)

            @staticmethod
            def getbool():
                return ra.random() < 0.5

            @staticmethod
            def getlistelement(list):
                return list[randomutil.getint(0, len(list) - 1)]

            @staticmethod
            def getdictkey(dict):
                return randomutil.getlistelement(list(dict.keys()))

            @staticmethod
            def getdictvalue(dict):
                return dict[randomutil.getdictkey(dict)]

        class serverutil:

            class wshttpserver(hsv.HTTPServer, wsv.WebsocketServer):

                @staticmethod
                def init():
                    pass

                ''' SEALED FUNCTIONS, DO NOT MODIFY OR OVERRIDE '''

                def __init__(self, addr=('127.0.0.1', 80), handler=None):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    if sk.socket(sk.AF_INET,
                                 sk.SOCK_STREAM).connect_ex(addr) == 0:
                        raise Exception(' '.join(['端口', str(addr[1]), '已被占用']))
                    hsv.HTTPServer.__init__(self, addr, handler)
                    self.host = addr[0]
                    self.port = self.socket.getsockname()[1]
                    self.clients = []
                    self.id_counter = 0
                    self._deny_clients = False
                    self.set_fn_new_client(handler.wsonconnect)
                    self.set_fn_client_left(handler.wsonclose)
                    self.set_fn_message_received(handler.wsonreceive)

                def start(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    taskutil.setloop(time=60.0,
                                     func=serverutil.wshttphandler.wspingloop)
                    taskutil.setasync(func=hsv.HTTPServer.serve_forever,
                                      args=(self, ))

            class wshttphandler(hsv.BaseHTTPRequestHandler,
                                wsv.WebSocketHandler):

                @staticmethod
                def init():
                    pass

                @staticmethod
                def sendresponse(resp, ssid, url, body):
                    result = httprouter.getresponse(ssid, url, body, resp)
                    if not result:
                        logutil.log(' '.join(['[无效]', url]), 'white', 'red')
                        #logutil.info(body)
                        result = httputil.getclearedbody(
                            None, 404, ' '.join(['未处理的请求:', url]))
                    if result in httpserver.onrespond:
                        httpserver.onrespond[result](ssid, url, body, result,
                                                     resp)
                    else:
                        serverutil.wshttphandler.sendzlibjson(
                            ssid, url, body, result, resp)

                @staticmethod
                def sendzlibjson(ssid, url, body, result, resp):
                    serverutil.wshttphandler.setheaders(
                        200, 'OK', httpserver.mime['json'], ssid, resp)
                    serverutil.wshttphandler.stream(result, resp, True)

                @staticmethod
                def sendtextjson(ssid, url, body, result, resp):
                    serverutil.wshttphandler.setheaders(
                        200, 'OK', httpserver.mime['json'], ssid, resp)
                    serverutil.wshttphandler.stream(result, resp)

                @staticmethod
                def sendmessage(ssid, url, body, result, resp):
                    pass

                @staticmethod
                def sendfile(ssid, url, body, result, resp):
                    ext = result.split('.')[-1]
                    if ext in httpserver.mime:
                        type = httpserver.mime[ext]
                    else:
                        type = httpserver.mime['txt']
                    serverutil.wshttphandler.setheaders(
                        200, 'OK', type, ssid, resp)
                    with open(result, 'rb') as file:
                        data = file.read()
                    serverutil.wshttphandler.stream(data, resp)

                @staticmethod
                def setheaders(code, msg, type, ssid, resp):
                    resp.send_response(code, msg)
                    resp.send_header('Content-Type', type)
                    resp.send_header('Set-Cookie',
                                     ''.join(['PHPSESSID=', ssid]))
                    resp.end_headers()

                @staticmethod
                def stream(data, resp, zlib=False):
                    fbytes = io.BytesIO()
                    if zlib:
                        fbytes.write(
                            zl.compress(data.encode(encoding='utf-8'),
                                        zl.DEFLATED))
                    else:
                        fbytes.write(data)
                    fbytes.seek(0)
                    sh.copyfileobj(fbytes, resp.wfile)

                @staticmethod
                def wspingloop():
                    pingmessage = {'type': 'ping', 'eventId': 'ping'}
                    for cs in httpserver.wspinghandler:
                        cs[1].send_message(cs[0],
                                           jsonutil.unparse(pingmessage))
                        logutil.info('')

                @staticmethod
                def wsonconnect(client, server):
                    httpserver.wspinghandler.append((client, server))

                @staticmethod
                def wsonreceive(client, server, message):
                    print(message)

                @staticmethod
                def wsonclose(client, server):
                    csindex = 0
                    for cs in httpserver.wspinghandler:
                        if cs[0]['id'] == client['id']:
                            del httpserver.wspinghandler[csindex]
                            csindex += 1

                ''' SEALED FUNCTIONS, DO NOT MODIFY OR OVERRIDE '''

                def __init__(self, socket, addr, server):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    self.default_request_version = 'HTTP/1.1'
                    self._send_lock = th.Lock()
                    hsv.BaseHTTPRequestHandler.__init__(
                        self, socket, addr, server)

                def GET(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    url = self.path
                    ssidattr = 'PHPSESSID'
                    cookies = self.getcookies()
                    ssid = str(cookies[ssidattr]
                               )[str(cookies[ssidattr]).find(ssidattr) +
                                 len(ssidattr) +
                                 1:] if ssidattr in cookies else ''
                    body = ''
                    logutil.log(' '.join(['[', str(ssid), ']', url]), 'white')
                    serverutil.wshttphandler.sendresponse(
                        self, ssid, url, body)

                def POST(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    url = self.path
                    ssidattr = 'PHPSESSID'
                    cookies = self.getcookies()
                    ssid = str(cookies[ssidattr]
                               )[str(cookies[ssidattr]).find(ssidattr) +
                                 len(ssidattr) +
                                 1:] if ssidattr in cookies else ''
                    bodylen = int(self.headers.get('Content-Length') or 0)
                    body = jsonutil.parse(
                        zl.decompress(self.rfile.read(bodylen)))
                    logutil.log(' '.join(['[', str(ssid), ']', url]), 'white')
                    serverutil.wshttphandler.sendresponse(
                        self, ssid, url, body)

                def handle(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    self.read_http_headers()
                    if not hasattr(self, 'headers'):
                        return
                    if self.headers.get('Upgrade') == 'websocket':
                        self.iswsconn = True
                        wsv.WebSocketHandler.handle(self)
                    else:
                        self.iswsconn = False
                        hsv.BaseHTTPRequestHandler.handle(self)

                def handshake(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    try:
                        key = self.headers.get('Sec-WebSocket-Key')
                    except KeyError:
                        self.keep_alive = False
                        return
                    response = self.make_handshake_response(key)
                    with self._send_lock:
                        self.handshake_done = self.request.send(
                            response.encode())
                    self.valid_client = True
                    self.server._new_client_(self)

                def getcookies(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    return hck.SimpleCookie(self.headers.get('Cookie'))

                def finish(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    if not hasattr(self, 'iswsconn'):
                        return
                    if self.iswsconn:
                        wsv.WebSocketHandler.finish(self)
                    else:
                        hsv.BaseHTTPRequestHandler.finish(self)

                def read_http_headers(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    try:
                        self.raw_requestline = self.rfile.readline(65537)
                        if len(self.raw_requestline) > 65536:
                            self.requestline = ''
                            self.request_version = ''
                            self.command = ''
                            self.send_error(h.HTTPStatus.REQUEST_URI_TOO_LONG)
                            return
                        if not self.raw_requestline:
                            self.close_connection = True
                            return
                        self.headers = hcl.parse_headers(
                            self.rfile, self.MessageClass)
                    except hcl.LineTooLong as err:
                        self.send_error(
                            h.HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
                            'Line too long', str(err))
                    except hcl.HTTPException as err:
                        self.send_error(
                            h.HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE,
                            'Too many headers', str(err))

                def parse_request(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    self.command = None
                    self.request_version = version = self.default_request_version
                    self.close_connection = True
                    requestline = str(self.raw_requestline, 'iso-8859-1')
                    requestline = requestline.rstrip('\r\n')
                    self.requestline = requestline
                    words = requestline.split()
                    if len(words) == 0:
                        return False
                    if len(words) >= 3:
                        version = words[-1]
                        try:
                            if not version.startswith('HTTP/'):
                                raise ValueError
                            base_version_number = version.split('/', 1)[1]
                            version_number = base_version_number.split('.')
                            if len(version_number) != 2:
                                raise ValueError
                            version_number = int(version_number[0]), int(
                                version_number[1])
                        except (ValueError, IndexError):
                            self.send_error(
                                h.HTTPStatus.BAD_REQUEST,
                                'Bad request version (%r)' % version)
                            return False
                        if version_number >= (
                                1, 1) and self.protocol_version >= 'HTTP/1.1':
                            self.close_connection = False
                        if version_number >= (2, 0):
                            self.send_error(
                                h.HTTPStatus.HTTP_VERSION_NOT_SUPPORTED,
                                'Invalid HTTP version (%s)' %
                                base_version_number)
                            return False
                        self.request_version = version
                    if not 2 <= len(words) <= 3:
                        self.send_error(
                            h.HTTPStatus.BAD_REQUEST,
                            'Bad request syntax (%r)' % requestline)
                        return False
                    command, path = words[:2]
                    if len(words) == 2:
                        self.close_connection = True
                        if command != 'GET':
                            self.send_error(
                                h.HTTPStatus.BAD_REQUEST,
                                'Bad HTTP/0.9 request type (%r)' % command)
                            return False
                    self.command, self.path = command, path
                    conntype = self.headers.get('Connection', '')
                    if conntype.lower() == 'close':
                        self.close_connection = True
                    elif (conntype.lower() == 'keep-alive'
                          and self.protocol_version >= 'HTTP/1.1'):
                        self.close_connection = False
                    expect = self.headers.get('Expect', '')
                    if (expect.lower() == '100-continue'
                            and self.protocol_version >= 'HTTP/1.1'
                            and self.request_version >= 'HTTP/1.1'):
                        if not self.handle_expect_100():
                            return False
                    return True

                def handle_one_request(self):
                    ''' 
                    SEALED FUNCTION,
                    DO NOT MODIFY OR OVERRIDE.
                    '''
                    try:
                        if not self.parse_request():
                            return
                        mname = self.command
                        if not hasattr(self, mname):
                            self.send_error(
                                h.HTTPStatus.NOT_IMPLEMENTED,
                                'Unsupported method (%r)' % self.command)
                            return
                        method = getattr(self, mname)
                        method()
                        self.wfile.flush()
                    except TimeoutError as e:
                        self.log_error('Request timed out: %r', e)
                        self.close_connection = True
                        return

                def log_message(self, format, *args):
                    pass

        class taskutil:

            class loopholder:
                pool = []
                tid = 0
                running = True

                def __init__(self):
                    self.pool = None
                    taskutil.loopholder.tid += 1
                    self.tid = taskutil.loopholder.tid
                    taskutil.loopholder.pool.append(self)

            @staticmethod
            def init():
                pass

            @staticmethod
            def setdelay(time=1e-6, func=None, args=()):
                timer = th.Timer(interval=time, function=func, args=args)
                timer.start()

            @staticmethod
            def setasync(func=None, args=()):
                task = th.Thread(target=func, args=args)
                task.start()

            @staticmethod
            def setloop(time=1e-6, func=None, args=(), looper=None):
                if not looper:
                    looper = taskutil.loopholder()
                if looper.running:
                    timer = th.Timer(interval=time,
                                     function=taskutil.setloop,
                                     args=(
                                         time,
                                         func,
                                         args,
                                         looper,
                                     ))
                    timer.start()
                func(*args)
                return looper.tid

            @staticmethod
            def stoploop(tid):
                taskindex = 0
                for looper in taskutil.loopholder.pool:
                    if looper.tid == tid:
                        looper.running = False
                    del taskutil.loopholder.pool[taskindex]
                    taskindex += 1

        class timeutil:

            @staticmethod
            def init():
                pass

            @staticmethod
            def gettime():
                return timeutil.formattime(t.localtime())

            @staticmethod
            def getdate():
                return timeutil.formatdate(dt.datetime.today())

            @staticmethod
            def gettimestamp():
                return int(t.time())

            @staticmethod
            def formattime(time):
                return t.strftime('%H-%M-%S', time)

            @staticmethod
            def formatdate(date):
                return date.strftime('%Y-%m-%d')

        class watermarkutil:
            name = None
            version = None
            zh_cn = [
                'https://sns.oddba.cn', '', '本作品完全免费', '禁止用于商业用途', '',
                '当前版本无技术支持', '请自行承担使用风险'
            ]

            @staticmethod
            def init():
                watermarkutil.setinfo()
                watermarkutil.draw()

            @staticmethod
            def setinfo():
                ca.init(autoreset=True)
                watermarkutil.name = 'SPT-iDk Python'
                watermarkutil.version = '1.0.0'
                watermarkutil.zh_cn.insert(
                    0, ' '.join([watermarkutil.name, watermarkutil.version]))
                sys.stdout.write(' '.join([
                    '\x1b]2;', watermarkutil.name, watermarkutil.version,
                    '\x07'
                ]))
                sys.stdout.write('\u001B[2J\u001B[0;0f')
                sys.stdout.flush()

            @staticmethod
            def draw():
                result = []
                longest = 0
                for text in watermarkutil.zh_cn:
                    length = watermarkutil.length(text)
                    if length > longest:
                        longest = length
                line = '━' * longest
                result.append(''.join(['┏━', line, '━┓']))
                for text in watermarkutil.zh_cn:
                    spacesize = longest - watermarkutil.length(text)
                    spacetext = ''.join([text, ' ' * spacesize])
                    result.append(''.join(['┃ ', spacetext, ' ┃']))
                result.append(''.join(['┗━', line, '━┛']))
                for text in result:
                    logutil.log(text, 'yellow')

            @staticmethod
            def length(string):
                length = 0
                for char in string:
                    if len(char.encode('utf-8')) == 1:
                        length += 1
                    else:
                        length += 2
                return length


class main:

    @staticmethod
    def init():
        main.alias()
        main.expose()
        main.start()

    @staticmethod
    def alias():

        global initializefunctions, itemevents, updatefunctions, saveinitfunctions, staticroutes, dynamicroutes, serverresponse
        initializefunctions = server.bindings.initializefunctions
        itemevents = server.bindings.itemevents
        updatefunctions = server.bindings.updatefunctions
        saveinitfunctions = server.bindings.saveinitfunctions
        staticroutes = server.bindings.staticroutes
        dynamicroutes = server.bindings.dynamicroutes
        serverresponse = server.bindings.serverresponse

        global botcallbacks, bundlecallbacks, configcallbacks, customizationcallbacks, databasecallbacks, dialoguecallbacks, gamecallbacks, handbookcallbacks, healthcallbacks, hideoutcallbacks, httpcallbacks, inraidcallbacks, insurancecallbacks, inventorycallbacks, itemeventcallbacks, launchercallbacks, locationcallbacks, matchcallbacks, notecallbacks, notifiercallbacks, presetbuildcallbacks, presetcallbacks, profilecallbacks, questcallbacks, ragfaircallbacks, repaircallbacks, savecallbacks, tradecallbacks, tradercallbacks, weathercallbacks, wishlistcallbacks
        botcallbacks = server.callbacks.botcallbacks
        bundlecallbacks = server.callbacks.bundlecallbacks
        configcallbacks = server.callbacks.configcallbacks
        customizationcallbacks = server.callbacks.customizationcallbacks
        databasecallbacks = server.callbacks.databasecallbacks
        dialoguecallbacks = server.callbacks.dialoguecallbacks
        gamecallbacks = server.callbacks.gamecallbacks
        handbookcallbacks = server.callbacks.handbookcallbacks
        healthcallbacks = server.callbacks.healthcallbacks
        hideoutcallbacks = server.callbacks.hideoutcallbacks
        httpcallbacks = server.callbacks.httpcallbacks
        inraidcallbacks = server.callbacks.inraidcallbacks
        insurancecallbacks = server.callbacks.insurancecallbacks
        inventorycallbacks = server.callbacks.inventorycallbacks
        itemeventcallbacks = server.callbacks.itemeventcallbacks
        launchercallbacks = server.callbacks.launchercallbacks
        locationcallbacks = server.callbacks.locationcallbacks
        matchcallbacks = server.callbacks.matchcallbacks
        notecallbacks = server.callbacks.notecallbacks
        notifiercallbacks = server.callbacks.notifiercallbacks
        presetbuildcallbacks = server.callbacks.presetbuildcallbacks
        presetcallbacks = server.callbacks.presetcallbacks
        profilecallbacks = server.callbacks.profilecallbacks
        questcallbacks = server.callbacks.questcallbacks
        ragfaircallbacks = server.callbacks.ragfaircallbacks
        repaircallbacks = server.callbacks.repaircallbacks
        savecallbacks = server.callbacks.savecallbacks
        tradecallbacks = server.callbacks.tradecallbacks
        tradercallbacks = server.callbacks.tradercallbacks
        weathercallbacks = server.callbacks.weathercallbacks
        wishlistcallbacks = server.callbacks.wishlistcallbacks

        global botconfig, healthconfig, hideoutconfig, httpconfig, inraidconfig, insuranceconfig, inventoryconfig, locationconfig, matchconfig, projectconfig, questconfig, ragfairconfig, repairconfig, saveconfig, traderconfig, weatherconfig
        botconfig = server.configs.botconfig
        healthconfig = server.configs.healthconfig
        hideoutconfig = server.configs.hideoutconfig
        httpconfig = server.configs.httpconfig
        inraidconfig = server.configs.inraidconfig
        insuranceconfig = server.configs.insuranceconfig
        inventoryconfig = server.configs.inventoryconfig
        locationconfig = server.configs.locationconfig
        matchconfig = server.configs.matchconfig
        projectconfig = server.configs.projectconfig
        questconfig = server.configs.questconfig
        ragfairconfig = server.configs.ragfairconfig
        repairconfig = server.configs.repairconfig
        saveconfig = server.configs.saveconfig
        traderconfig = server.configs.traderconfig
        weatherconfig = server.configs.weatherconfig

        global botcontroller, customizationcontroller, dialoguecontroller, gamecontroller, handbookcontroller, healthcontroller, hideoutcontroller, inraidcontroller, insurancecontroller, inventorycontroller, launchercontroller, locationcontroller, matchcontroller, notecontroller, notifiercontroller, paymentcontroller, playercontroller, presetbuildcontroller, presetcontroller, profilecontroller, questcontroller, ragfaircontroller, repaircontroller, repeatablequestcontroller, tradecontroller, tradercontroller, weathercontroller, wishlistcontroller
        botcontroller = server.controllers.botcontroller
        customizationcontroller = server.controllers.customizationcontroller
        dialoguecontroller = server.controllers.dialoguecontroller
        gamecontroller = server.controllers.gamecontroller
        handbookcontroller = server.controllers.handbookcontroller
        healthcontroller = server.controllers.healthcontroller
        hideoutcontroller = server.controllers.hideoutcontroller
        inraidcontroller = server.controllers.inraidcontroller
        insurancecontroller = server.controllers.insurancecontroller
        inventorycontroller = server.controllers.inventorycontroller
        launchercontroller = server.controllers.launchercontroller
        locationcontroller = server.controllers.locationcontroller
        matchcontroller = server.controllers.matchcontroller
        notecontroller = server.controllers.notecontroller
        notifiercontroller = server.controllers.notifiercontroller
        paymentcontroller = server.controllers.paymentcontroller
        playercontroller = server.controllers.playercontroller
        presetbuildcontroller = server.controllers.presetbuildcontroller
        presetcontroller = server.controllers.presetcontroller
        profilecontroller = server.controllers.profilecontroller
        questcontroller = server.controllers.questcontroller
        ragfaircontroller = server.controllers.ragfaircontroller
        repaircontroller = server.controllers.repaircontroller
        repeatablequestcontroller = server.controllers.repeatablequestcontroller
        tradecontroller = server.controllers.tradecontroller
        tradercontroller = server.controllers.tradercontroller
        weathercontroller = server.controllers.weathercontroller
        wishlistcontroller = server.controllers.wishlistcontroller

        global botgenerator, locationgenerator, pmclootgenerator
        botgenerator = server.generators.botgenerator
        locationgenerator = server.generators.locationgenerator
        pmclootgenerator = server.generators.pmclootgenerator

        global containerhelper, durabilitylimitshelper, inventoryhelper, itemhelper, questhelper, traderhelper, utilityhelper
        containerhelper = server.helpers.containerhelper
        durabilitylimitshelper = server.helpers.durabilitylimitshelper
        inventoryhelper = server.helpers.inventoryhelper
        itemhelper = server.helpers.itemhelper
        questhelper = server.helpers.questhelper
        traderhelper = server.helpers.traderhelper
        utilityhelper = server.helpers.utilityhelper

        global bundleloader, modloader
        bundleloader = server.loaders.bundleloader
        modloader = server.loaders.modloader

        global httprouter, imagerouter, itemeventrouter
        httprouter = server.routers.httprouter
        imagerouter = server.routers.imagerouter
        itemeventrouter = server.routers.itemeventrouter

        global databaseserver, httpserver, ragfairserver, saveserver
        databaseserver = server.servers.databaseserver
        httpserver = server.servers.httpserver
        ragfairserver = server.servers.ragfairserver
        saveserver = server.servers.saveserver

        global initializer, databaseutil, filesystemutil, hashutil, httputil, jsonutil, logutil, randomutil, serverutil, taskutil, timeutil, watermarkutil
        initializer = server.utils.initializer
        databaseutil = server.utils.databaseutil
        filesystemutil = server.utils.filesystemutil
        hashutil = server.utils.hashutil
        httputil = server.utils.httputil
        jsonutil = server.utils.jsonutil
        logutil = server.utils.logutil
        randomutil = server.utils.randomutil
        serverutil = server.utils.serverutil
        taskutil = server.utils.taskutil
        timeutil = server.utils.timeutil
        watermarkutil = server.utils.watermarkutil

    @staticmethod
    def expose():

        setattr(b, 'initializefunctions', initializefunctions)
        setattr(b, 'updatefunctions', updatefunctions)
        setattr(b, 'saveinitfunctions', saveinitfunctions)
        setattr(b, 'staticroutes', staticroutes)
        setattr(b, 'dynamicroutes', dynamicroutes)
        setattr(b, 'serverresponse', serverresponse)

        setattr(b, 'botcallbacks', botcallbacks)
        setattr(b, 'bundlecallbacks', bundlecallbacks)
        setattr(b, 'configcallbacks', configcallbacks)
        setattr(b, 'customizationcallbacks', customizationcallbacks)
        setattr(b, 'databasecallbacks', databasecallbacks)
        setattr(b, 'dialoguecallbacks', dialoguecallbacks)
        setattr(b, 'gamecallbacks', gamecallbacks)
        setattr(b, 'handbookcallbacks', handbookcallbacks)
        setattr(b, 'healthcallbacks', healthcallbacks)
        setattr(b, 'hideoutcallbacks', hideoutcallbacks)
        setattr(b, 'httpcallbacks', httpcallbacks)
        setattr(b, 'inraidcallbacks', inraidcallbacks)
        setattr(b, 'insurancecallbacks', insurancecallbacks)
        setattr(b, 'inventorycallbacks', inventorycallbacks)
        setattr(b, 'itemeventcallbacks', itemeventcallbacks)
        setattr(b, 'launchercallbacks', launchercallbacks)
        setattr(b, 'locationcallbacks', locationcallbacks)
        setattr(b, 'matchcallbacks', matchcallbacks)
        setattr(b, 'notecallbacks', notecallbacks)
        setattr(b, 'notifiercallbacks', notifiercallbacks)
        setattr(b, 'presetbuildcallbacks', presetbuildcallbacks)
        setattr(b, 'presetcallbacks', presetcallbacks)
        setattr(b, 'profilecallbacks', profilecallbacks)
        setattr(b, 'questcallbacks', questcallbacks)
        setattr(b, 'ragfaircallbacks', ragfaircallbacks)
        setattr(b, 'repaircallbacks', repaircallbacks)
        setattr(b, 'savecallbacks', savecallbacks)
        setattr(b, 'tradecallbacks', tradecallbacks)
        setattr(b, 'tradercallbacks', tradercallbacks)
        setattr(b, 'weathercallbacks', weathercallbacks)
        setattr(b, 'wishlistcallbacks', wishlistcallbacks)

        setattr(b, 'botconfig', botconfig)
        setattr(b, 'healthconfig', healthconfig)
        setattr(b, 'hideoutconfig', hideoutconfig)
        setattr(b, 'httpconfig', httpconfig)
        setattr(b, 'inraidconfig', inraidconfig)
        setattr(b, 'insuranceconfig', insuranceconfig)
        setattr(b, 'inventoryconfig', inventoryconfig)
        setattr(b, 'locationconfig', locationconfig)
        setattr(b, 'matchconfig', matchconfig)
        setattr(b, 'projectconfig', projectconfig)
        setattr(b, 'questconfig', questconfig)
        setattr(b, 'ragfairconfig', ragfairconfig)
        setattr(b, 'repairconfig', repairconfig)
        setattr(b, 'traderconfig', traderconfig)
        setattr(b, 'weatherconfig', weatherconfig)

        setattr(b, 'botcontroller', botcontroller)
        setattr(b, 'customizationcontroller', customizationcontroller)
        setattr(b, 'dialoguecontroller', dialoguecontroller)
        setattr(b, 'gamecontroller', gamecontroller)
        setattr(b, 'handbookcontroller', handbookcontroller)
        setattr(b, 'healthcontroller', healthcontroller)
        setattr(b, 'hideoutcontroller', hideoutcontroller)
        setattr(b, 'inraidcontroller', inraidcontroller)
        setattr(b, 'insurancecontroller', insurancecontroller)
        setattr(b, 'inventorycontroller', inventorycontroller)
        setattr(b, 'launchercontroller', launchercontroller)
        setattr(b, 'locationcontroller', locationcontroller)
        setattr(b, 'matchcontroller', matchcontroller)
        setattr(b, 'notecontroller', notecontroller)
        setattr(b, 'notifiercontroller', notifiercontroller)
        setattr(b, 'paymentcontroller', paymentcontroller)
        setattr(b, 'playercontroller', playercontroller)
        setattr(b, 'presetbuildcontroller', presetbuildcontroller)
        setattr(b, 'presetcontroller', presetcontroller)
        setattr(b, 'profilecontroller', profilecontroller)
        setattr(b, 'questcontroller', questcontroller)
        setattr(b, 'ragfaircontroller', ragfaircontroller)
        setattr(b, 'repaircontroller', repaircontroller)
        setattr(b, 'repeatablequestcontroller', repeatablequestcontroller)
        setattr(b, 'tradecontroller', tradecontroller)
        setattr(b, 'tradercontroller', tradercontroller)
        setattr(b, 'weathercontroller', weathercontroller)
        setattr(b, 'wishlistcontroller', wishlistcontroller)

        setattr(b, 'botgenerator', botgenerator)
        setattr(b, 'locationgenerator', locationgenerator)
        setattr(b, 'pmclootgenerator', pmclootgenerator)

        setattr(b, 'containerhelper', containerhelper)
        setattr(b, 'durabilitylimitshelper', durabilitylimitshelper)
        setattr(b, 'inventoryhelper', inventoryhelper)
        setattr(b, 'itemhelper', itemhelper)
        setattr(b, 'questhelper', questhelper)
        setattr(b, 'traderhelper', traderhelper)
        setattr(b, 'utilityhelper', utilityhelper)

        setattr(b, 'bundleloader', bundleloader)
        setattr(b, 'modloader', modloader)

        setattr(b, 'httprouter', httprouter)
        setattr(b, 'imagerouter', imagerouter)
        setattr(b, 'itemeventrouter', itemeventrouter)

        setattr(b, 'databaseserver', databaseserver)
        setattr(b, 'httpserver', httpserver)
        setattr(b, 'ragfairserver', ragfairserver)
        setattr(b, 'saveserver', saveserver)

        setattr(b, 'initializer', initializer)
        setattr(b, 'databaseutil', databaseutil)
        setattr(b, 'filesystemutil', filesystemutil)
        setattr(b, 'hashutil', hashutil)
        setattr(b, 'httputil', httputil)
        setattr(b, 'jsonutil', jsonutil)
        setattr(b, 'logutil', logutil)
        setattr(b, 'randomutil', randomutil)
        setattr(b, 'serverutil', serverutil)
        setattr(b, 'taskutil', taskutil)
        setattr(b, 'timeutil', timeutil)
        setattr(b, 'watermarkutil', watermarkutil)

    @staticmethod
    def start():
        logutil.init()
        watermarkutil.init()
        initializer.init()
        modloader.init()


if __name__ == '__main__':
    main.init()
