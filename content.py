PROFILE = {
    "name": "Reva Hristo Wiki Fonseca",
    "title": "IT Infrastructure & AIOps Specialist",
    "location": "Bogor, Indonesia",
    "email": "reva.wiki@gmail.com",
    "linkedin": "https://linkedin.com/in/revawiki",
    "github": "https://github.com/revawiki",
    "twitter": "https://x.com/revawiki",
    "instagram": "https://www.instagram.com/revawiki/",
    "whatsapp": "https://wa.me/6285714602966",
    "credly": "https://www.credly.com/users/reva-hristo-wiki-fonseca/badges/credly",
    "summary": (
        "IT Infrastructure & AIOps engineer with 7+ years architecting and operating "
        "enterprise-scale cloud infrastructure for B2B and B2C production systems serving "
        "millions of users. Currently leading AIOps R&D for Indonesia's largest telco cloud "
        "operation, architecting a multi-agent AI system spanning 20+ AWS accounts and 10+ "
        "Kubernetes clusters. Focused on turning manual, headcount-bound operations into "
        "resilient, self-optimizing systems."
    ),
}

STACK = [
    {
        "group": "AIOps & AI Automation",
        "items": ["Agent Swarm", "RAG & Knowledge Base", "MCP Server", "Human-in-the-Loop",
                   "Amazon Bedrock", "Microsoft Copilot Studio", "Azure AI Foundry", "Dify",
                   "n8n", "UiPath", "Power Platform"],
    },
    {
        "group": "Cloud Platforms",
        "items": ["AWS", "Azure", "GCP", "Alibaba Cloud", "Digital Ocean"],
    },
    {
        "group": "Infrastructure & Orchestration",
        "items": ["Kubernetes", "Docker", "Terraform", "Ansible", "Puppet"],
    },
    {
        "group": "CI/CD & DevOps",
        "items": ["GitOps Workflow", "Zero-Downtime Deployment", "Bitbucket Pipeline", "Jenkins", "GitLab"],
    },
    {
        "group": "Observability",
        "items": ["Grafana", "Datadog", "New Relic", "Elastic", "Prometheus", "PagerDuty"],
    },
    {
        "group": "Security & DevSecOps",
        "items": ["Guardrails", "Sonarqube", "Snyk", "Trivy", "Jfrog", "Teleport", "Vault", "Burpsuite"],
    },
    {
        "group": "Scripting & Languages",
        "items": ["Python", "Bash", "PowerShell", "Go"],
    },
    {
        "group": "ITSM & Documentation",
        "items": ["ServiceNow", "BMC Remedy", "Confluence", "Notion", "SharePoint"],
    },
]

FEATURED_WORK = [
    {
        "name": "Unified L1 Autopilot",
        "tagline": "An AI-driven operations layer turning reactive IT Ops into autonomous, human-governed triage and remediation.",
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
    },
]

EXPERIENCE = [
    {
        "company": "Tech Mahindra",
        "company_url": "https://www.techmahindra.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=techmahindra.com",
        "role": "Senior System Engineer",
        "period": "January 2025 – Present",
        "location": "Jakarta, Indonesia",
        "narrative": (
            "Directing AIOps R&D for one of Indonesia's largest telco cloud operations, leading "
            "a 4-engineer team to design AI-driven automation across 20+ AWS accounts and 10+ "
            "Kubernetes clusters — covering anomaly detection, AI-assisted root-cause analysis, "
            "pre-deployment safeguards, and revenue-protecting failover automation."
        ),
        "stack": ["AWS", "Kubernetes", "RAG & Knowledge Base", "MCP Server", "Agent Swarm",
                    "Human-in-the-Loop", "Grafana", "Python"],
        "featured_link": True,
    },
    {
        "company": "PT HM Sampoerna Tbk.",
        "company_url": "https://www.sampoerna.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=sampoerna.com",
        "role": "Senior DevOps Engineer",
        "period": "June 2024 – December 2024",
        "location": "Jakarta, Indonesia",
        "narrative": (
            "Led a 7-engineer team through a console-to-Terraform migration with consistent GitOps "
            "branching, standardized 40+ legacy AWS accounts to global governance standards, and "
            "drove SEA-region cost optimization while automating away recurring service-request toil."
        ),
        "stack": ["AWS", "Terraform", "GitOps Workflow", "Jenkins", "Security & Governance"],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=telkom.co.id",
        "role": "DevOps Lead",
        "period": "April 2022 – May 2024",
        "location": "Jakarta, Indonesia",
        "narrative": (
            "Promoted to lead a 4-engineer DevOps team, architecting a multi-tenant AWS ECS "
            "platform off 100+ monolithic EC2 deployments, with a regional migration and CI/CD "
            "rollout that cut both infrastructure cost and deployment time substantially."
        ),
        "stack": ["AWS ECS", "Bitbucket Pipeline", "Cloud Migration"],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=telkom.co.id",
        "role": "Technical Support Engineer",
        "period": "August 2020 – April 2022",
        "location": "Jakarta, Indonesia",
        "narrative": (
            "Supported a cloud incubation initiative, building Terraform and Ansible-provisioned "
            "pipelines that significantly cut deployment time, and introducing Grafana-based "
            "observability that improved incident response."
        ),
        "stack": ["Terraform", "Ansible", "Grafana"],
    },
    {
        "company": "BRIN — Aviation Technology Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "System Administrator",
        "period": "June 2020 – August 2020",
        "location": "Bogor, Indonesia",
        "narrative": (
            "Rebuilt a legacy HPC lab by repairing 20+ broken nodes, restoring research capacity "
            "without new hardware spend."
        ),
        "stack": ["HPC Infrastructure", "Hardware Diagnostics"],
    },
    {
        "company": "BRIN — Informatics Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "Junior System Administrator",
        "period": "February 2019 – December 2019",
        "location": "Bogor, Indonesia",
        "narrative": (
            "Rolled out Puppet-based configuration management across a 40+ node HPC environment, "
            "replacing ad-hoc manual configuration with consistent, repeatable infrastructure state."
        ),
        "stack": ["Puppet", "Configuration Management"],
    },
    {
        "company": "PT Griya Mitra Persada",
        "company_url": "https://www.griyamitrapersada.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=griyamitrapersada.com",
        "role": "IT Support Lead",
        "period": "July 2018 – September 2018",
        "location": "Bogor, Indonesia",
        "narrative": (
            "Led a 5-person on-site IT support team across 50+ end-devices through the Asian "
            "Games event, ensuring zero-downtime operations under high-visibility pressure."
        ),
        "stack": ["IT Support", "End-Device Management"],
    },
]

EDUCATION = [
    {"school": "UIN Syarif Hidayatullah Jakarta", "degree": "Bachelor of Computer Science", "year": "2023"},
    {"school": "SMKN 3 Bogor", "degree": "Vocational Diploma in Computer Networks", "year": "2016"},
]
