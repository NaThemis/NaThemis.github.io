import os
import json

posts = [
    {
        "filename": "20230301_LesEchos_IA.md",
        "title": "IA: Anticiper les évolutions des traités européens",
        "date": "2023-03-01",
        "categories": '["AI"]',
        "tags": '["AI", "Europe", "Treaties", "Compliance"]',
        "slug": "ia-anticiper-evolutions-traites-europeens",
        "body": """
:gavel:

AI isn't just a tech issue; it's a geopolitical chessboard.

I recently shared my thoughts in Les Echos on why we need to stay ahead of European treaty evolutions regarding AI. We're not just waiting for the rules to be written—we're anticipating them and building the infrastructure to match.

Want to build compliant, future-proof AI strategies without the headache? I've outlined the roadmap. Let's dig in.

👉 Read the full opinion: [Les Echos - Opinion IA](https://www.lesechos.fr/idees-debats/cercle/opinion-ia-anticiper-les-evolutions-des-traites-europeens-1907725) | [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_opinion-ia-anticiper-les-%C3%A9volutions-des-activity-7038507219105009665-8V5j)

<!-- more -->
"""
    },
    {
        "filename": "20230601_Meetup_Annonces_Data.md",
        "title": "Analyse des Annonces Data: Microsoft Fabric & Databricks",
        "date": "2023-06-01",
        "categories": '["Data Platforms"]',
        "tags": '["Microsoft Fabric", "Databricks", "Data Architecture", "Meetup"]',
        "slug": "analyse-annonces-data-fabric-databricks",
        "body": """
:rocket:

The data landscape is shifting fast, and if you blink, you'll miss the revolution.

I recently broke down the massive announcements from Microsoft Build (hello, Microsoft Fabric!) and the Databricks Data + AI Summit. No marketing fluff—just the hardcore technical implications and what this means for your data architecture.

Ready to level up your platform? Let's decode the hype together.

👉 Catch the insights from the Meetup: [Eventbrite Link](https://www.eventbrite.fr/e/billets-build-microsoft-et-data-ai-summit-les-nouveautes-data-a-ne-pas-rater-656554541307) | [LinkedIn Post](https://www.linkedin.com/in/nathalie-fouet/recent-activity/all/)

<!-- more -->
"""
    },
    {
        "filename": "20230501_Responsible_AI_Dashboard.md",
        "title": "Le Dashboard Responsible AI de Microsoft",
        "date": "2023-05-01",
        "categories": '["AI"]',
        "tags": '["Microsoft", "Ethics", "Responsible AI", "Dashboard"]',
        "slug": "dashboard-responsible-ai-microsoft",
        "body": """
:mag:

Talking about Responsible AI is easy; actually implementing it is where the real work begins.

I took a deep dive into Microsoft's Responsible AI Dashboard to see what's under the hood. I cut through the noise to show you exactly how to use these tools to build models you can trust and explain. 

Building ethical AI doesn't have to be a drag—let's make it a competitive advantage.

👉 Discover how to implement it: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_le-dashboard-responsible-ai-de-microsoft-activity-7071763060683628544-TgT6)

<!-- more -->
"""
    },
    {
        "filename": "20230302_DataPlatform_Silos.md",
        "title": "Data Platform: Améliorer la Traçabilité en Cassant les Silos",
        "date": "2023-03-02",
        "categories": '["Data Platforms"]',
        "tags": '["Data Architecture", "Traceability", "Silos"]',
        "slug": "data-platform-tracabilite-silos",
        "body": """
:factory:

Silos are where data goes to die. If you want real product traceability, it's time to tear down the walls.

In this replay, I walk through the exact architecture and mindset needed to build a modern Data Platform that actually connects the dots. We're talking end-to-end visibility, no excuses. 

Let's get your data working as a single, unstoppable unit.

👉 Watch the replay: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_replay-am%C3%A9liorer-la-tra%C3%A7abilit%C3%A9-de-vos-activity-7038502738892083201-hLze)

<!-- more -->
"""
    },
    {
        "filename": "20230201_IA_Act_Approche.md",
        "title": "L'IA Act arriverait dans 2 ans!",
        "date": "2023-02-01",
        "categories": '["AI"]',
        "tags": '["AI Act", "ChatGPT", "Regulation", "Europe"]',
        "slug": "ia-act-arriverait-dans-2-ans",
        "body": """
:scales:

The AI Act is coming in two years, and the clock is ticking.

ChatGPT, DALL-E, and Lensa have forced the regulators' hands, but you don't need to panic—you need to prepare. I've broken down what this means for your AI initiatives and how to stay ahead of the compliance curve without stifling innovation.

Let's build AI that's not just powerful, but bulletproof.

👉 Get ready for what's coming: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_chatgpt-dalle2-lensaai-activity-7027320992385363969-cueE)

<!-- more -->
"""
    },
    {
        "filename": "20230101_Meetup_Cellenza_IA_Responsable.md",
        "title": "Meetup Cellenza: L'IA responsable et de confiance",
        "date": "2023-01-01",
        "categories": '["AI"]',
        "tags": '["Meetup", "Cellenza", "Responsible AI", "Ethics"]',
        "slug": "meetup-cellenza-ia-responsable",
        "body": """
:handshake:

Trust isn't given; it's engineered.

At the Cellenza Meetup, I took the stage to tackle the real-world execution of Responsible and Trustworthy AI. We didn't just talk philosophy—we talked frameworks, guardrails, and how to deploy generative AI without losing your shirt (or your reputation).

Let's build AI systems that people can actually rely on.

👉 Check out the discussion: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_event-ia-chatgpt-activity-7019252597207236608-UuQv)

<!-- more -->
"""
    },
    {
        "filename": "20221201_USEU_Data_Transfers.md",
        "title": "US-EU Data Transfers: The Saga Continues",
        "date": "2022-12-01",
        "categories": '["Data Platforms"]',
        "tags": '["Data Privacy", "US-EU", "Compliance"]',
        "slug": "us-eu-data-transfers-saga-continues",
        "body": """
:earth_africa:

The US-EU data transfer saga is the soap opera that never ends, but your compliance strategy can't run on drama.

I've broken down the latest twists, what it means for your transatlantic data flows, and how to keep your operations running smoothly while the regulators figure things out. No legal jargon—just clear, actionable intelligence.

Let's keep your data moving safely.

👉 Read my take on the latest update: [LinkedIn Post](https://www.linkedin.com/feed/update/urn:li:activity:7009046997714223104)

<!-- more -->
"""
    },
    {
        "filename": "20220301_Run_Projet_IA_MLOps.md",
        "title": "Run d'un Projet IA: Garder sous contrôle le cycle de vie d'un modèle ML",
        "date": "2022-03-01",
        "categories": '["AI"]',
        "tags": '["MLOps", "Model Lifecycle", "Production"]',
        "slug": "run-projet-ia-cycle-de-vie-mlops",
        "body": """
:gear:

Building an ML model is the easy part; keeping it alive in production is where champions are made.

I've shared my battle-tested strategies for mastering the 'Run' phase of an AI project. From drift detection to seamless MLOps life cycles, I'll show you how to keep your models sharp and your operations flawless. 

Let's take control of your ML lifecycle.

👉 Dive into the operational roadmap: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_build-run-ai-activity-6909465708540166144-S6Nb)

<!-- more -->
"""
    },
    {
        "filename": "20220201_Droit_Humanitaire_Technologies.md",
        "title": "Le Droit Humanitaire face aux nouvelles technologies",
        "date": "2022-02-01",
        "categories": '["Cyber"]',
        "tags": '["Humanitarian Law", "Cyberattacks", "Tech Ethics"]',
        "slug": "droit-humanitaire-nouvelles-technologies",
        "body": """
:globe_with_meridians:

When cutting-edge tech collides with International Humanitarian Law, the stakes couldn't be higher.

I recently explored how cyberattacks and AI are forcing a rewrite of the rules of engagement. It's a complex, high-stakes arena, but I've distilled the critical intersections you need to understand. 

Let's bring some clarity to the chaos of modern digital warfare.

👉 Explore the intersection of tech and law: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_dih-ia-cyberattack-activity-6900025336893968384-le-T)

<!-- more -->
"""
    },
    {
        "filename": "20211001_Clash_Microsoft_IA.md",
        "title": "Le Clash Microsoft - IA: From scratch vs. sur étagère",
        "date": "2021-10-01",
        "categories": '["AI"]',
        "tags": '["Microsoft", "Build vs Buy", "Strategy", "YouTube"]',
        "slug": "clash-microsoft-ia-scratch-vs-etagere",
        "body": """
:boxing_glove:

Build from scratch or buy off-the-shelf? It's the ultimate AI showdown.

In this 'Clash' episode, we throw down over the pros, cons, and hidden traps of custom AI versus out-of-the-box Microsoft solutions. I don't pull punches—I'll give you the straight talk you need to make the right architectural call for your business.

Ring the bell, let's go.

👉 Watch the clash: [YouTube Video](https://www.youtube.com/watch?v=tNak1SiVe4c&list=PL5Kprdw8GhxfuvGtkGyhZ-o9AjfPxgoGw&index=6) | [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_leclash-data-bigdata-activity-6856168138753531904-YxLT)

<!-- more -->
"""
    },
    {
        "filename": "20210501_Proposals_European_Commission_IA.md",
        "title": "L'Essentiel des propositions de la commission européenne pour une IA de confiance",
        "date": "2021-05-01",
        "categories": '["AI"]',
        "tags": '["European Commission", "Trustworthy AI", "Regulation"]',
        "slug": "essentiel-propositions-commission-europeenne-ia",
        "body": """
:bulb:

The European Commission has laid its cards on the table for Trustworthy AI.

Trying to decipher the proposals on your own? Don't bother. I've done the heavy lifting, stripping away the bureaucratic noise to give you the absolute essentials. We'll look at the risk categories, the obligations, and how to position your projects for success.

Let's make compliance your superpower.

👉 Get the essential breakdown: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_les-propositions-de-la-commission-europ%C3%A9enne-activity-6797930536045215744-v0pL)

<!-- more -->
"""
    },
    {
        "filename": "20201001_MLFlow_Pratique.md",
        "title": "MLFlow, explication pratique",
        "date": "2020-10-01",
        "categories": '["AI", "Data Platforms"]',
        "tags": '["MLFlow", "Data Science", "Tutorial", "MLOps"]',
        "slug": "mlflow-explication-pratique",
        "body": """
:bar_chart:

If your data science team is drowning in unversioned notebooks and untracked experiments, it's time for an intervention. Enter MLFlow.

In this practical breakdown, I cut through the theory and show you exactly how to wield MLFlow to orchestrate your machine learning pipeline like a pro. Say goodbye to chaos and hello to reproducibility. 

Let's get to work.

👉 Check out the practical guide: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_mlflow-data-mlops-activity-6721722449966235648-stf8)

<!-- more -->
"""
    },
    {
        "filename": "20200201_Deep_Metric_Learning.md",
        "title": "Livre Blanc: Détectez des visages dans une vidéo grâce au Deep Metric Learning",
        "date": "2020-02-01",
        "categories": '["AI"]',
        "tags": '["Computer Vision", "Deep Metric Learning", "Whitepaper"]',
        "slug": "livre-blanc-deep-metric-learning-visages",
        "body": """
:tv:

Facial detection in video isn't just about throwing data at a neural network—it's an art.

In this whitepaper, I tear down the mechanics of using Deep Metric Learning to achieve pinpoint accuracy. Whether you're building security systems or advanced analytics, I'll walk you through the architecture that gets results.

Time to sharpen your computer vision skills. Let's dive in.

👉 Download the whitepaper: [LinkedIn Post](https://www.linkedin.com/posts/nathalie-fouet_data-ia-deepmetriclearning-activity-6635825659484622848-uBGF)

<!-- more -->
"""
    }
]

template = """---
date:
    created: {date}
    updated: {date}
draft: false
authors: 
    - nathalie
categories: {categories}
readtime: 5
slug: {slug}
tags: 
{tags_formatted}
---

# {title}

{body}
"""

output_dir = "/Users/nfo/Documents/sources/nathemiswebsite/docs/posts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for post in posts:
    tags_list = json.loads(post["tags"])
    tags_formatted = "\n".join([f"    - {tag}" for tag in tags_list])
    
    content = template.format(
        date=post["date"],
        categories=post["categories"],
        slug=post["slug"],
        title=post["title"],
        tags_formatted=tags_formatted,
        body=post["body"]
    )
    
    file_path = os.path.join(output_dir, post["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created/Updated: {file_path}")
