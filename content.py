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
    "resume": "static/assets/Reva-Wiki-CV.pdf",
    "photo": None,
    "summary": (
        "IT Infrastructure & AIOps engineer with 7+ years architecting and operating "
        "enterprise-scale cloud infrastructure for B2B and B2C production systems serving "
        "millions of users. Currently leading AIOps R&D for Indonesia's largest telco cloud "
        "operation, architecting a multi-agent AI system spanning 20+ AWS accounts and 10+ "
        "Kubernetes clusters. Focused on turning manual, headcount-bound operations into "
        "resilient, self-optimizing systems."
    ),
}

DOMAIN_KNOWLEDGE = [
    {
        "group": "AIOps & AI Automation",
        "items": ["Agent Swarm", "RAG & Knowledge Base", "MCP Server", "Human-in-the-Loop", "Guardrails"],
    },
    {
        "group": "Cloud Platforms",
        "items": ["Container Orchestration", "Hybrid Architecture", "Infrastructure as Code", "Cost Optimization"],
    },
    {
        "group": "DevOps",
        "items": ["CI/CD Pipeline", "GitOps Workflow", "Zero-Downtime Deployment", "Monitoring, Logging & Traceability"],
    },
]

TOOLS = [
    {"group": "AI Automation", "items": ["Amazon Bedrock", "Microsoft Copilot Studio", "Azure AI Foundry", "Dify", "n8n", "UIPath", "Power Platform"]},
    {"group": "Cloud", "items": ["AWS", "Azure", "GCP", "Alibaba Cloud", "Digital Ocean"]},
    {"group": "Orchestration & Containers", "items": ["Kubernetes", "Docker", "Containerd", "Amazon ECS", "Amazon EKS"]},
    {"group": "IaC & Config Management", "items": ["Terraform", "Ansible", "Puppet", "Amazon CloudFormation", "Helm", "Foreman", "Kickstart"]},
    {"group": "CI/CD", "items": ["Bitbucket Pipeline", "Jenkins", "GitLab", "GitLab Runner", "Flux", "CloudBees CI"]},
    {"group": "Observability", "items": ["Grafana", "Datadog", "New Relic", "Elastic", "Prometheus", "PagerDuty", "Amazon CloudWatch", "OpsGenie", "Fluentbit", "OpenTelemetry"]},
    {"group": "DevSecOps", "items": ["Brinqa", "Faradaysec", "Sonarqube", "Snyk", "Trivy", "Jfrog", "Teleport", "Vault", "Burpsuite", "Invicti", "OWASP ZAP", "Nikto", "Dependency Check", "DefectDojo", "git-secrets", "Nuclei", "Polaris", "Soteri"]},
    {"group": "Scripting & Languages", "items": ["Python", "Bash", "PowerShell", "Go"]},
    {"group": "ITSM & Documentation", "items": ["ServiceNow", "BMC Remedy", "Confluence", "Notion", "SharePoint", "Jira", "Trello"]},
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
        "narrative": (
            "Leading R&D for AIOps and automation within the IT Cloud Operations team supporting "
            "one of Indonesia's largest telecommunications providers, directing a 4-engineer team "
            "across 20+ AWS accounts and 10+ Kubernetes clusters. Built automatic anomaly detection "
            "and AI-assisted root-cause analysis that cut MTTD to ≤5 minutes and MTTR to ≤10 minutes, "
            "introduced an automatic MOP checker that nearly tripled change-request throughput, and "
            "developed an AWS Direct Connect failover solution preventing IDR 79B+ in yearly revenue "
            "loss. Unified these workflows into a single agentic AI system with RAG, MCP servers, and "
            "human-in-the-loop governance — work recognized with Tech Mahindra's Innovator of the "
            "Month award."
        ),
        "stack": ["AWS", "Amazon RDS", "RDS for PostgreSQL", "RDS for MySQL", "Amazon Linux", "Python",
                   "Bash", "n8n", "Power Platform", "Dify", "Amazon Bedrock", "Microsoft Copilot Studio",
                   "Azure AI Foundry", "Docker", "Containerd", "Kubernetes", "Amazon EKS", "Amazon ECS",
                   "Terraform", "Amazon CloudFormation", "Helm", "Amazon SSM", "GitLab Enterprise",
                   "AWS CodeCommit", "GitLab Runner", "Jenkins", "Flux", "Amazon ECR", "Grafana",
                   "Datadog", "Amazon CloudWatch", "Fluentbit", "OpenTelemetry", "Prometheus",
                   "SharePoint", "Microsoft Teams", "WhatsApp"],
        "featured_link": True,
    },
    {
        "company": "PT HM Sampoerna Tbk.",
        "company_url": "https://www.sampoerna.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=sampoerna.com",
        "role": "Senior DevOps Engineer",
        "period": "June 2024 – December 2024",
        "narrative": (
            "Maintained SLAs for HM Sampoerna's application portfolio (AYO SRC, promotional sites, "
            "internal tools) as part of the IT Solution Architect team, leading a 7-engineer group "
            "through a console-to-Terraform migration with consistent GitOps branching and "
            "standardizing 40+ legacy AWS accounts to global Philip Morris International compliance "
            "standards. Transformed manual ClickOps processes into automated workflows, cutting "
            "~1-2 hours of daily repetitive tasks via Jenkins automation, while driving SEA-region "
            "cloud costs down ~55% through regular cost evaluation and optimization — alongside "
            "mentoring junior engineers and improving the team's documentation practices."
        ),
        "stack": ["AWS", "Amazon Aurora MySQL", "Amazon DocumentDB", "Amazon Linux", "Python", "Bash",
                   "PowerShell", "Docker", "Kubernetes", "Amazon ECS", "Terraform", "Amazon SSM",
                   "Amazon Secrets Manager", "Vault", "OpenVPN", "Bitbucket", "Jenkins", "CloudBees CI",
                   "Amazon ECR", "Jfrog Artifactory", "Soteri", "Polaris", "Trivy", "Jfrog Xray",
                   "Sonarqube", "Invicti", "Brinqa", "Grafana", "Elastic", "Amazon CloudWatch",
                   "New Relic", "PagerDuty", "OpsGenie", "Confluence", "SharePoint", "Microsoft Teams",
                   "ServiceNow"],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=www.telkom.co.id",
        "role": "DevOps Lead",
        "period": "April 2022 – May 2024",
        "narrative": (
            "Promoted to lead the 4-engineer Infrastructure (DevOps) team for Telkom's Netmonk "
            "product suite (Netmonk Prime, Netmonk HI, DTP), architecting a multi-tenant AWS ECS "
            "platform off 100+ monolithic EC2 deployments and rearchitecting the regional footprint "
            "from Singapore to Jakarta for a ~70% infrastructure cost reduction. Built CI/CD "
            "automation via Bitbucket pipelines that cut deployment time from ~10 to ~5 minutes, "
            "while improving deployment frequency, lead time, and change failure rate through "
            "provisioning automation, resource/log/trace monitoring, and IAM-driven security "
            "integration across the development lifecycle."
        ),
        "stack": ["AWS", "Digital Ocean", "Aiven", "MongoDB Atlas", "Amazon RDS", "Ubuntu",
                   "Amazon Linux", "Windows Server", "PostgreSQL", "MySQL", "MongoDB", "InfluxDB",
                   "Prometheus", "Timescale", "Redis", "Kafka", "OpenSearch", "Python", "Bash", "Go",
                   "Docker", "Kubernetes", "Amazon ECS", "Amazon EKS", "Terraform", "Ansible", "Consul",
                   "Vault", "Teleport", "AWS Systems Manager", "Bitbucket", "GitLab", "Bitbucket Pipeline",
                   "Jenkins", "Dockerhub", "Nuclei", "git-secrets", "Dependency Check", "Snyk", "Trivy",
                   "Sonarqube", "OWASP ZAP", "Nikto", "Faraday", "DefectDojo", "Grafana", "Datadog",
                   "Confluence", "Notion", "Jira", "Slack", "Discord"],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=www.telkom.co.id",
        "role": "Technical Support Engineer",
        "period": "August 2020 – April 2022",
        "narrative": (
            "Provided technical support and network-monitoring deployment services for Netmonk "
            "clients ranging from small businesses to large enterprises — installing, configuring, "
            "and troubleshooting Netmonk Basic, training users, and prototyping solutions while "
            "feeding client feedback back to the product team. Built Terraform and Ansible-provisioned "
            "pipelines that cut deployment time from ~40 to ~10 minutes, and introduced Grafana-based "
            "observability that reduced MTTR from ~30 to ~15 minutes."
        ),
        "stack": ["AWS", "Ubuntu", "Windows Server", "Grafana", "Jira", "Slack", "Trello"],
    },
    {
        "company": "BRIN — Aviation Technology Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "System Administrator",
        "period": "June 2020 – August 2020",
        "narrative": (
            "Built a 50-node HPC lab from scratch for Pustekbang's Aviation Technology Research "
            "Center — planning the network topology, repairing or replacing 20+ broken nodes to "
            "avoid new hardware spend, automating OS installation and configuration across the "
            "cluster, and setting up rack layout, cable management, and remote monitoring, with full "
            "documentation of every node's status."
        ),
        "stack": ["CentOS", "Ubuntu", "Windows 10", "Kickstart", "C3 (Cluster Control)", "Supermicro",
                   "Cisco Switch", "LAN", "WLAN"],
    },
    {
        "company": "BRIN — Informatics Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "Junior System Administrator",
        "period": "February 2019 – December 2019",
        "narrative": (
            "Assisted in maintaining a 40+ node HPC lab for BRIN's Informatics Research Center — "
            "running regular checks to identify and repair damaged nodes, automating new node and "
            "cluster installations, and rolling out Puppet-based configuration management to keep "
            "software and configuration consistent across the cluster, with daily condition reports "
            "on lab infrastructure."
        ),
        "stack": ["CentOS", "Ubuntu", "Windows Hyper-V", "Puppet", "Kickstart", "C3 (Cluster Control)",
                   "Foreman", "Cisco Switch", "Aruba Switch", "MikroTik", "LAN", "WLAN"],
    },
    {
        "company": "PT Griya Mitra Persada",
        "company_url": "https://www.griyamitrapersada.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=griyamitrapersada.com",
        "role": "IT Support Lead",
        "period": "July 2018 – September 2018",
        "narrative": (
            "Led a 5-person on-site IT support team responsible for 50+ end-devices (laptops, "
            "printers, PCs, copiers) at Pakansari Stadium during the 2018 Asian Games — installing, "
            "testing, and auditing devices, coordinating with other divisions during events, and "
            "keeping every device operational throughout the matches."
        ),
        "stack": ["Windows 10", "Windows 7", "Canon Printers", "HP Printers & Copiers",
                   "HP Laptops & AIO PCs", "TP-Link Access Point", "LAN", "WLAN"],
    },
]

EDUCATION = [
    {"school": "UIN Syarif Hidayatullah Jakarta", "degree": "Bachelor of Computer Science", "year": "2023"},
    {"school": "SMKN 3 Bogor", "degree": "Vocational Diploma in Computer Networks", "year": "2016"},
]
