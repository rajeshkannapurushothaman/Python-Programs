# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:09:55 2023

@author: rajeshkanna
"""

from langdetect import detect

def detect_language(content):
    try:
        language = detect(content)
        return language
    except:
        return None

# Example usage
text = "The Tribunal held that the measures taken by Peru resulted in the expropriation of Claimant's assets based on their “impact and duration.” Claimant's initial investment was equal to approximately US$400,000, and TSG was quickly one of the leading entities in the Peruvian fishing industry with annual sales reaching approximately US$20 million. As a result of the audit, the tax authorities had demanded a payment of 95 tax units (approximately US$12 million plus interest). Tax authorities notified 15 separate banks to freeze TSG's accounts. Peru presented evidence indicating that TSG could have paid cash to address the tax measures and to maintain its access to the banking system. The Tribunal found that Peru knew or should have know how TSG obtained financing for its business and that this sort of measure would “hit the heart of TSG's operations,” strangling the normal ways through which TSG could obtain capital. The Tribunal echoed the language in <it>Archer Daniels Midland et. al. v. Mexico</it> to the effect that expropriation “may occur through actions that are different from a direct expropriation of tangible assets, such as taxes.” The Tribunal explained that, generally, a State is not responsible for the loss suffered by an individual as a consequence of good faith taxes, but it is also established that under international and Peruvian law, the State's conduct in this respect is not without limits, which include the principles of proportionality and rationality. As a result, the Tribunal concluded that Peru's actions were arbitrary."
language = detect_language(text)
if language:
    print("Detected language:", language)
else:
    print("Language detection failed.")
