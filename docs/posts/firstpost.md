---
date:
    created: 2025-09-01
    updated: 2025-09-01
draft: false
categories: [AI, Data Platforms]
readtime: 15
---

# AI Agents & Data Platforms

How will AI Agents revolutionize Data Platforms? Are AI Agents the end of centralized data platforms and the Lakehouse? 

<!-- more -->

For years, companies have been aware of the strategic value of data. Clive Humby already expressed this when he said that " _Data is the new oil_ ", thus highlighting the need not only to collect data, but also to transform, refine and analyze it to derive actionable insights.

The evolution of data management architectures has followed this logic, moving from **_Data Warehouses_** to **_Data Lakes_**, then _to_ **_Lakehouses_** and, more recently, **_to Data Mesh_**. These models have sought to improve the accessibility, governance and scalability of data to support the growing needs of companies.

Thanks for reading! Subscribe for free to receive new posts and support my work.

However, a new paradigm seems to be emerging with the rise of **_Artificial Intelligence (AI)_** agents. These are challenging centralized data platforms and **_Lakehouse_** architectures, not to replace them, but to complement them. The **_Data Fabric_** architecture then appears as a hybrid and modular approach allowing a more agile integration of **_AI Agents_** into the existing ecosystem.

**An emerging contradiction?**

While the evolution of data architectures seemed to be following a linear trajectory towards more decentralization with Data _Mesh_, the rise of AI agents raises the question of the future of traditional data platforms.

## Data Platforms: Evolution of architectures and emergence of new approaches.

**_Data_** **_platforms_** play a critical role in data management and analysis within companies. Depending on their needs, their volume of data and their uses, different architectures have developed over time.

**_Typical_** **_data platform structures_** depend on business needs, data volumes, and usage, but they are typically based on recurring components and architectures. The image below shows the main types of **_Data_** **_Platform structures_** :

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3396758c-cfde-4b23-95e4-485bea6e6e60_468x263.png)



](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3396758c-cfde-4b23-95e4-485bea6e6e60_468x263.png)

**In this context, 3 tools are made up of these Data Platforms.**

**_Tool 1 - Data Warehouse_**

A _Data Warehouse_ is a centralized database designed for analyzing structured data. It stores transformed and cleansed data from various sources in a unified format, facilitating business analytics and BI (_Business Intelligence_) reporting.

**_Features:_**

- Relational model optimized for complex SQL queries.
    
- Highly governed and validated data.
    
- _Use cases:_ Reporting, analytical dashboards.
    
- _Examples:_ Snowflake, Google BigQuery, Amazon Redshift.
    

**_Tool 2 - Data Lake_**

A _Data Lake_ allows large amounts of raw data to be stored in its native format, whether structured, semi-structured, or unstructured. This approach is especially useful for advanced analytics and _machine learning_.

**_Features_**_:_

- Massive, low-cost storage, often cloud-based.
    
- Raw data retention with on-demand transformation.
    
- _Use cases:_ Big Data analysis, AI, log management, IoT data.
    
- _Examples:_ Amazon S3, Azure Data Lake, Hadoop HDFS.
    

**_Tool 3 - Data Lakehouse_**

The _Lakehouse_ is a hybrid approach combining the strengths of _the Data Warehouse_ and the _Data Lake_. It combines the flexibility and scalability of raw data storage from a _Data Lake_ with the advanced management features and governance mechanisms of a _Data Warehouse,_ ensuring high data quality.

**_Features_**_:_

- Storage of raw and structured data in a single environment.
    
- Support for SQL queries and advanced processing (_Python, Spark, new analytics, and machine learning usecases_).
    
- Strengthened governance with metadata management and ACID transactions (_e.g. Delta Lake_).
    
- **_Use case_**_:_ Businesses that require both analytics and operational data management.
    
- **_Examples_**_:_ Databricks, Delta Lake.
    

These tools are particularly effective for operational analysis and reporting. However, they rely on centralization and involve the duplication of data, which can lead to governance issues, data quality issues, and in some cases, foster the proliferation of data silos.

**In this sense, a more global data strategy is essential, which can be found in the 2 methodologies below.**

**_Methodology 1 - Data Mesh_**

_Data mesh_ is a decentralized architecture where data is managed as a product by the business teams that create it. Rather than a single, centralized platform, each business area (sales, marketing, logistics, etc.) is responsible for its own data and exposes it via standardized interfaces.

**_Features_**_:_

- Reduced silos and improved scalability.
    
- Empower business teams with a global governance framework.
    
- _Use case:_ Businesses with distributed teams and complex needs.
    

**_Methodology 2 - Data Fabric_**

Unlike previous models, this approach creates a web of intelligent connections between different data sources, regardless of format or location. AI plays a key role in automating the integration, governance, and management of data flows.

**_Features_**_:_

- Intelligent integration and interconnection of data sources.
    
- Automation of discovery, governance, and security processes.
    
- _Use case:_ Organizations with heterogeneous systems requiring smooth and optimized interconnection.
    

Historically, **_Data Platforms_** have followed a common principle: centralize, transform, and qualify data before sharing it securely. This approach offers undeniable advantages in terms of governance, access protection and scalability in the face of growing data volumes. However, it also has limitations, including high maintenance costs, the risk of errors related to duplication and a lack of flexibility in the face of new uses.

## A challenge to traditional data platforms?

The emergence of generative AI is disrupting this traditional vision of data management. **_AI Agent_** models such as ChatGPT, Microsoft Copilot or Gemini demonstrate that it is possible to access and exploit data without going through aggregation and centralized transformation. This capability challenges the very necessity of traditional data platforms and questions their relevance in a world where users can, with just a few clicks, create their own **_AI Agents_** connected directly to existing data sources.

**Should we abandon Data Platforms?**

While decentralization and direct access to data are attractive, **_Data Platforms_** retain essential advantages:

- **Protection of data sources**
    
    - Prevention of over-use of _golden sources_, avoiding the risk of overloading and performance degradation.
        
    - Role of "shield" between users and critical databases.
        
    - Centralized access control, ensuring secure and structured management.
        
- **Governance and security**
    
    - Consistent enforcement of security policies across the enterprise.
        
    - Simplification of the traceability of access and use of data.
        
- **Data management and valorization**
    
    - Facilitating cross-referencing of multiple sources.
        
    - Maintain a _data catalog_ for a unified view of data assets.
        
    - Monitoring of data lineage and ensuring data quality.
        
- **Coordination of _AI Agents_**
    
    - Need for a common foundation (such as _Lakehouses_) to structure and orchestrate interactions between AI and data.
        
    - Ensuring consistent management of global access and processing policies.
        
- **Regulatory Compliance**
    
    - Responding to centralization obligations imposed by various regulations.
        
    - Simplify audits and compliance requirements.
        

**Augmented Data Platforms with AI Agents**

**_Data Platforms_** will not disappear, but their role is evolving. The challenge is no longer just to centralize, but to enable controlled and intelligent access to data, while integrating the capabilities of generative AI. The key lies in a hybrid approach, combining flexibility, governance and scalability to meet the new challenges posed by **_AI_** and the decentralization of uses. Unlike traditional platforms, which centralize and transform data before it is used, AI agents operate directly on the sources, analyzing and acting in real time.

**A role of augmentation rather than replacement.**

Rather than replacing **_Data Platforms_**, **_AI agents_** enrich them by automating complex tasks, improving data analysis, and making it easier for users and systems to interact. However, their proliferation raises new challenges in terms of governance, security and storage of the data generated. Their integration brings several key benefits:

- **Process automation** : **_AI Agents_** optimize analytical workflows and accelerate decision-making.
    
- **Summary and recommendations** : They allow you to process and summarize large volumes of information for more efficient use.
    
- **Hybridization of architectures** : An approach combining centralization and decentralization seems to be emerging.
    

**AI agents closer to data**

Training AI agents directly on **_CRUD_** (Create, Read, Update, Delete) sources opens up new perspectives:

- **Improved reliability** : Reduced risk from multiple transformations.
    
- **Increased responsiveness** : Ability to act instantly on data updated in real time.
    
- **Proximity to databases**: Just as **_AI_** is increasingly integrated into operating systems, these AI Agents could move closer to databases, optimizing their interaction with unmodified data.
    

**Challenges to be overcome**

The integration of **_AI Agents_** into data management requires a robust infrastructure and strict governance mechanisms:

- **Security and control** : Ensure the integrity and confidentiality of the data handled.
    
- **Data quality** : Reliability is based on rigorous validation and clean-up processes at the source.
    
- **Regulation and governance** : Supervise the use of data to ensure compliance with the standards in force.
    

## What type of architecture can integrate this decentralized structure of AI Agents?

A **hybrid approach combining centralization and decentralization** is more likely.

### AI Lakehouses

**_Lakehouses_** can serve as a foundation for **_AI Agents_**, with a better integration of AI bricks into the Lakehouse: The emergence of **_AI Lakehouses_**, combining centralized governance and flexibility, thus making it possible to fully exploit the potential of AI agents while mastering issues related to data quality and security.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3c6f2b8-993e-41fb-b728-2b7a5ac459cf_468x233.png)



](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc3c6f2b8-993e-41fb-b728-2b7a5ac459cf_468x233.png)

### Data Fabric & AI Agents: Intelligent and Agile Architecture

In the face of data fragmentation and system sprawl, **_the Data Fabric_** architecture is emerging as a hybrid and modular solution, offering a unified and accessible view of all data, regardless of its location (_on-premise_, cloud, multi-cloud). Its virtualized approach eliminates the need for complex migrations, reducing costs and accelerating data time-to-value.

**Synergy with AI Agents**

Integrating **_AI Agents_** into a **_Data Fabric_** architecture increases efficiency by automating metadata management, improving data quality, and optimizing analytics workflows:

- **Unified Access & Self-Service** : Allows business and technical users to access data without worrying about formats or locations.
    
- **Automation & Intelligence** : The use of machine learning to continuously catalog, govern, and enrich data.
    
- **Governance & Security** : Proactive monitoring, anomaly detection and compliance compliance (_RBAC, ABAC, encryption, anonymization_).
    
- **Process optimization** : Improved queries and data pipelines with predictive analytics.
    

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b6d3e1c-c70c-47c0-aef2-537bd1ca94ab_461x258.png)



](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b6d3e1c-c70c-47c0-aef2-537bd1ca94ab_461x258.png)

**An Answer to the Challenges of Fragmented Data**

Companies are faced with a paradox: "the proliferation of systems that are supposed to structure data only accentuates its dispersion and complicates its use".

The **_Data Fabric_** architecture solves this problem by harmonizing data access without imposing migration constraints:

- **Seamless interconnection** between databases, data lakes, SaaS applications, and real-time workflows.
    
- **An agile and scalable model** that can be adapted to business needs without weighing down the infrastructure.
    
- **A secure and proactive approach**, integrating cybersecurity and access tracking for optimized risk management.
    

**Towards a New Generation of Data Platforms**

By integrating AI agents, the **_Data Fabric_** architecture goes beyond simple data management and becomes a true engine of automated intelligence. It combines the **flexibility of _the Data Mesh_**, the **analytical capacity of _the Lakehouses_** and enhanced **cybersecurity**, laying the foundations for a new generation of smarter and more integrated data platforms.

AI and even more so agents are profoundly changing our approach to the organization of data flows in the company. Training AI agents directly on CRUD sources will improve the relevance and accuracy of analyses by eliminating potentially error-prone intermediaries. However, this requires a focus on data governance, security, and infrastructure to ensure a successful implementation within this new generation of data platform "Data Fabric".

## Towards a Hybrid and Intelligent Data Ecosystem

The **_Data Fabric_** architecture, enriched by **_AI Agents_**, marks a transition to more agile, automated, and intelligent data management. In a world where companies are looking for **real-time insights**, **optimized data quality** and **strengthened governance**, this approach is becoming an essential strategic lever.

The future is moving towards a **hybrid model** where each brick plays a complementary role:

- **_AI Agents_** bring intelligence and autonomy by automating flows and analyses.
    
- **Centralized platforms** ensure coordination, compliance, and governance.
    
- **Lakehouses** serve as a technical foundation for unifying and structuring data.
    
- **The _Data Fabric architecture_** streamlines the integration of AI bricks thanks to its modular and interconnected architecture.
    

By combining these elements, companies have a **flexible and efficient data ecosystem**, capable of adapting to the new challenges of an increasingly complex and dynamic data management. 🚀

**_Sources_**

• [Data Warehouse vs. Data Lake vs. Data Lakehouse vs. Data Mesh](https://www.linkedin.com/pulse/data-warehouse-vs-lake-lakehouse-mesh-ashish-bijawat)

• [https://www.cncf.io/blog/2022/12/08/data-mesh-vs-data-fabric-a-tale-of-two-new-data-paradigms/?ref=dailydev](https://www.cncf.io/blog/2022/12/08/data-mesh-vs-data-fabric-a-tale-of-two-new-data-paradigms/?ref=dailydev)

• [https://thenewstack.io/stage-a-productivity-revolution-with-process-automation-ai-and-data-fabric/?ref=dailydev](https://thenewstack.io/stage-a-productivity-revolution-with-process-automation-ai-and-data-fabric/?ref=dailydev)

• https://appian.com/fr/learn/topics/data-fabric/what-is-data-fabric

• https://www.hopsworks.ai/post/the-ai-lakehouse

• [https://www.databricks.com/blog/lakehouse-ai](https://www.databricks.com/blog/lakehouse-ai)