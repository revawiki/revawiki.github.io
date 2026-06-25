PROFILE = {
    "name": "Reva Hristo Wiki Fonseca",
    "title": "IT Infrastructure & AIOps Specialist",
    "location": "Bogor, Indonesia",
    "email": "reva.wiki@gmail.com",
    "linkedin": "https://linkedin.com/in/revawiki",
    "github": "https://github.com/revawiki",
    "summary": (
        "Seasoned engineer with 7+ years of experience designing, managing, and optimizing "
        "enterprise-scale cloud infrastructure across multiple industries, supporting critical "
        "B2B and B2C production applications serving millions of users. Proven track record "
        "delivering AI-driven automation transformation for IT operations, most notably "
        "architecting a multi-agent AI system covering 20+ AWS accounts and 10+ Kubernetes "
        "clusters for Indonesia's largest telco cloud operations, recognized as a stellar AI "
        "enablement example across the IT infrastructure department. Currently directing AIOps "
        "R&D to streamline cloud operations through AI and automation for consistent SLA "
        "attainment."
    ),
}

CORE_COMPETENCIES = [
    {
        "group": "AIOps & AI Automation",
        "items": ["Agent Swarm", "RAG & Knowledge Base", "MCP Server", "Human-in-the-Loop", "Guardrails"],
    },
    {
        "group": "Cloud Infrastructure",
        "items": ["Container Orchestration", "Hybrid Architecture", "Infrastructure as Code", "Cost Optimization"],
    },
    {
        "group": "DevOps",
        "items": ["CI/CD Pipeline", "GitOps Workflow", "Zero-Downtime Deployment", "Monitoring, Logging & Traceability"],
    },
]

FEATURED_PROJECT = {
    "name": "Unified L1 Autopilot",
    "tagline": (
        "An AI-driven operations layer transforming traditional IT Ops from reactive, "
        "headcount-bound ticket handling into autonomous, human-governed triage and remediation."
    ),
    "role": "R&D Lead, Tech Mahindra — Jan 2025 to Present",
    "problem": (
        "Scaling enterprise IT operations at the pace of the business inevitably runs into a "
        "‘human ceiling’: operational reliability becomes hostage to manual triage and the "
        "limits of human fatigue. This creates a ‘linear trap’ where growth is tethered "
        "to headcount, increasing systemic risk and operational noise with every new integration. "
        "I led the R&D effort to break that trap by shifting from manual, ticket-driven operations "
        "to AI-supported, and eventually autonomous, orchestration."
    ),
    "pillars": [
        {
            "title": "Intelligent Triage & Predictive Risk Mitigation",
            "desc": (
                "Real-time telemetry analysis pinpoints root causes automatically, converting "
                "reactive troubleshooting into predictive, data-driven detection, and "
                "neutralizing misconfigurations before they impact service availability."
            ),
        },
        {
            "title": "Fiscal Governance & Benchmarking",
            "desc": (
                "Automated optimization workflows and resource scheduling realize significant "
                "compute savings, backed by continuous performance benchmarking against "
                "architectural best practices."
            ),
        },
        {
            "title": "Autonomous Security & Self-Healing",
            "desc": (
                "Continuous compliance checks against security and configuration baselines "
                "eliminate manual audit cycles, scaling from automated patching toward "
                "autonomous issue remediation."
            ),
        },
        {
            "title": "Augmented Engineering Workflows",
            "desc": (
                "Context-aware knowledge retrieval auto-generates documentation (MOPs, "
                "playbooks, RCAs), while every AI-proposed action is queued for human review "
                "before execution — keeping institutional control intact."
            ),
        },
    ],
    "approach": (
        "Rather than building a single monolithic bot, the Autopilot is structured around the "
        "same roles and responsibilities a mature IT operations team already has — a "
        "Technical Operations Engineer, a Service Desk Analyst, a SOC Engineer, a Technical "
        "Writer, and a FinOps Analyst — each mapped to a distinct, scoped capability. This "
        "keeps coverage systematic and accountability clear as the system grows, following a "
        "deliberate crawl-walk-run rollout rather than a single 'big bang' deployment."
    ),
    "outcomes": [
        {"metric": "4x", "label": "Faster MTTR via AI-driven autonomous diagnostics"},
        {"metric": "60%", "label": "Compute cost reduction from automated resource governance"},
        {"metric": "IDR 79B+", "label": "Annual revenue loss prevented via automated failover"},
        {"metric": "75%", "label": "Toil elimination on backup and recovery test cycles"},
    ],
    "note": "Figures reflect actual client adoption; results may vary based on internal scope.",
}

EXPERIENCE = [
    {
        "company": "Tech Mahindra",
        "role": "Senior System Engineer",
        "period": "January 2025 – Present",
        "narrative": (
            "Directing AIOps R&D for one of Indonesia's largest telco cloud operations, leading "
            "a 4-engineer team to design AI-driven automation across 20+ AWS accounts and 10+ "
            "Kubernetes clusters. The work progressed in stages: first building automatic anomaly "
            "detection to catch issues before they escalate, then layering AI-assisted root-cause "
            "analysis on top, then extending into pre-deployment safeguards and revenue-protecting "
            "failover automation. Recognized by Tech Mahindra's Chief People Officer as Innovator "
            "of the Month for client-acknowledged AI enablement impact."
        ),
        "bullets": [
            "Led R&D initiative with a team of 4 engineers to develop AI-driven automation workflows that streamline day-to-day cloud operations on production workload across 20+ AWS accounts and 10+ Kubernetes clusters.",
            "Built an automatic infrastructure anomaly detection which reduced MTTD from ~20 to ≤ 5 minutes; further iteration integrated AI-assisted first-level RCA which reduced MTTR from ~30 to ≤ 10 minutes.",
            "Introduced an automatic MOP (Method-of-Procedure) checker that flags invalid steps pre-deployment, reducing review cycles from ~60 to ~20 minutes and increasing team throughput from 1-2 to 4+ change requests per day.",
            "Developed an automatic AWS Direct Connect failover solution that eliminated manual switchover procedures, preventing IDR 79B+ in yearly revenue loss from recurrent fiber optic outage incidents.",
            "Architected a unified AI operations ecosystem integrating RAG knowledge base, MCP servers, and human-in-the-loop governance, establishing a scalable foundation for the CloudOps AI development continuation.",
            "Recognized as Innovator of the Month by Tech Mahindra's Chief People Officer in June 2025, driven by client-acknowledged AI enablement initiatives in cloud operations.",
        ],
        "featured_link": True,
    },
    {
        "company": "PT HM Sampoerna Tbk.",
        "role": "Senior DevOps Engineer",
        "period": "June 2024 – December 2024",
        "narrative": (
            "Brought in to bring order to inherited infrastructure: led 7 engineers through a "
            "console-to-Terraform migration for highly critical applications, enforcing a "
            "consistent GitOps branching strategy across environments. In parallel, audited 40+ "
            "legacy AWS accounts against global Philip Morris International security and "
            "governance standards, and drove SEA-region cost optimization through rightsizing "
            "and reservation strategy — freeing budget while also automating away repetitive "
            "daily service-request toil."
        ),
        "bullets": [
            "Led a team of 7 engineers in migrating highly critical application infrastructure from console-based to Terraform, enforcing consistent GitOps branching strategy across dev, staging, and production environments.",
            "Evaluated and standardized inherited legacy AWS configurations across 40+ accounts, ensuring alignment with global Philip Morris International security and governance standards.",
            "Reduced AWS infrastructure costs for SEA region by ~55% through rightsizing, reservation optimization, and elimination of redundant and unused resources.",
            "Eliminated 1-2 hours of daily repetitive service request tasks through targeted Jenkins automations, improving team operational efficiency by freeing team capacity for higher-value work.",
        ],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "role": "DevOps Lead",
        "period": "April 2022 – May 2024",
        "narrative": (
            "Promoted to lead the DevOps initiative, directing 4 engineers through an "
            "architectural shift from 100+ monolithic EC2 deployments to a scalable, "
            "multi-tenant AWS ECS platform. The transition included a full regional migration "
            "from Singapore to Jakarta that cut infrastructure costs by ~70%, alongside a "
            "Bitbucket CI/CD rollout that halved deployment time."
        ),
        "bullets": [
            "Promoted to led the DevOps initiative leading a team of 4 engineers to architect an AWS ECS-based platform transitioning from 100+ monolithic AWS EC2 deployments to a scalable multi-tenancy cloud-native setups.",
            "Reduced AWS infrastructure costs by ~70% by rearchitecting regional migration from Singapore to Jakarta.",
            "Cut deployment time from ~10 to ~5 minutes through Bitbucket CI/CD pipeline implementation.",
        ],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "role": "Technical Support Engineer",
        "period": "August 2020 – April 2022",
        "narrative": (
            "Supported the Netmonk incubation as the team's cloud technical lead, building "
            "Terraform and Ansible-provisioned pipelines that quartered deployment time, and "
            "introducing Grafana-based observability that halved MTTR — groundwork that "
            "later justified the move into a full DevOps leadership role."
        ),
        "bullets": [
            "Reduced deployment time from ~40 to ~10 minutes through Terraform + Ansible provisioned pipelines.",
            "Reduced MTTR from ~30 to ~15 minutes through implementation of Grafana-based observability system.",
        ],
    },
    {
        "company": "BRIN — Aviation Technology Research Center",
        "role": "System Administrator",
        "period": "June 2020 – August 2020",
        "narrative": (
            "Took on the rebuild of a legacy HPC lab that had fallen into disrepair, repairing "
            "20+ broken nodes and restoring research capacity without requiring new hardware "
            "spend."
        ),
        "bullets": [
            "Rebuilt legacy HPC lab infrastructure by repairing 20+ broken nodes, avoiding new hardware purchases.",
        ],
    },
    {
        "company": "BRIN — Informatics Research Center",
        "role": "Junior System Administrator",
        "period": "February 2019 – December 2019",
        "narrative": (
            "Brought configuration management discipline to a 40+ node HPC environment by "
            "rolling out Puppet, replacing ad-hoc manual configuration with consistent, "
            "repeatable infrastructure state."
        ),
        "bullets": [
            "Implemented configuration management using Puppet, ensuring infra consistency across 40+ HPC nodes.",
        ],
    },
    {
        "company": "PT Griya Mitra Persada",
        "role": "IT Support Lead",
        "period": "July 2018 – September 2018",
        "narrative": (
            "Led a 5-person on-site IT support team responsible for 50+ end-devices through the "
            "high-stakes, high-visibility Asian Games event — an early lesson in operating "
            "under pressure with zero tolerance for downtime."
        ),
        "bullets": [
            "Achieved smooth operations leading a team of 5 across 50+ end-devices throughout the Asian Games event.",
        ],
    },
]

EDUCATION = [
    {"school": "UIN Syarif Hidayatullah Jakarta", "degree": "Bachelor of Computer Science", "year": "2023"},
    {"school": "SMKN 3 Bogor", "degree": "Vocational Diploma in Computer Networks", "year": "2016"},
]

TECHNICAL_SKILLS = [
    {"group": "AI Automation", "items": ["Amazon Bedrock", "Microsoft Copilot Studio", "Azure AI Foundry", "Dify", "n8n", "UIPath", "Power Platform"]},
    {"group": "Cloud", "items": ["AWS", "Azure", "GCP", "Alibaba Cloud", "Digital Ocean"]},
    {"group": "Orchestration & Containers", "items": ["Kubernetes", "Docker"]},
    {"group": "IaC & Config Management", "items": ["Terraform", "Ansible", "Puppet"]},
    {"group": "CI/CD", "items": ["Bitbucket Pipeline", "Jenkins", "GitLab"]},
    {"group": "Observability", "items": ["Grafana", "Datadog", "New Relic", "Elastic", "Prometheus", "PagerDuty"]},
    {"group": "DevSecOps", "items": ["Brinqa", "Faradaysec", "Sonarqube", "Snyk", "Trivy", "Jfrog", "Teleport", "Vault", "Burpsuite"]},
    {"group": "Scripting & Languages", "items": ["Python", "Bash", "PowerShell", "Go"]},
    {"group": "ITSM & Documentation", "items": ["ServiceNow", "BMC Remedy", "Confluence", "Notion", "SharePoint"]},
]

CERTIFICATIONS = [
    "AWS Certified Gen AI Developer – Professional",
    "AWS Certified DevOps Engineer – Professional",
    "AWS Certified Solution Architect – Professional",
    "AWS Certified ML Engineer – Associate",
    "AWS Certified SysOps Administrator – Associate",
    "AWS Certified Solution Architect – Associate",
    "AWS Certified AI Practitioner",
    "AWS Certified Cloud Practitioner",
    "Microsoft Certified: Azure Fundamentals",
]
