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
        "A boy from a rural corner of Indonesia, now thriving to become the country's go-to AIOps "
        "expert, one automated workflow at a time. Grounded in years of cloud infrastructure work, "
        "now growing into agentic AI to make IT operations more resilient, so engineers can spend "
        "less time firefighting and more time building."
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
    {"group": "Orchestration & Containers", "items": ["Kubernetes", "Docker"]},
    {"group": "IaC & Config Management", "items": ["Terraform", "Ansible", "Puppet"]},
    {"group": "CI/CD", "items": ["Bitbucket Pipeline", "Jenkins", "GitLab"]},
    {"group": "Observability", "items": ["Grafana", "Datadog", "New Relic", "Elastic", "Prometheus", "PagerDuty"]},
    {"group": "DevSecOps", "items": ["Brinqa", "Faradaysec", "Sonarqube", "Snyk", "Trivy", "Jfrog", "Teleport", "Vault", "Burpsuite"]},
    {"group": "Scripting & Languages", "items": ["Python", "Bash", "PowerShell", "Go"]},
    {"group": "ITSM & Documentation", "items": ["ServiceNow", "BMC Remedy", "Confluence", "Notion", "SharePoint"]},
]

FEATURED_WORK = [
    {
        "name": "Unified L1 Copilot Platform",
        "tagline": "A centralized AI ecosystem combining RAG, memory, and an MCP farm to unify various automation workflows, turning reactive IT Ops into autonomous, human-governed triage and remediation.",
        "role": "Associated with Tech Mahindra",
        "challenge": (
            "Enterprise IT operations rarely fail from a single cause. They're stretched across "
            "multiple concurrent workloads, run by teams with limited headcount, and pushed to "
            "process a high volume of daily change requests, all while gaps in observability "
            "oversight make problems harder to catch early. Together, these pressures compound "
            "manual triage fatigue, and in the long run, this risks business continuity if a "
            "critical incident slips through unnoticed."
        ),
        "action": (
            "To tackle these challenges, we built a centralized AIOps engine that brings IT "
            "infrastructure monitoring, ITSM/CMDB, internal documentation, and communication "
            "channels together into a single correlation layer, instead of leaving them as "
            "disconnected tools each engineer has to check separately. This consolidation matters "
            "because it lets telemetry and tickets feed one AI model that cross-references a "
            "knowledge base and memory store for context, then executes through an MCP-connected "
            "automation layer. Every action it proposes is still routed through a human "
            "approve/reject step before reaching production, so the system closes blind spots in "
            "observability without giving up institutional control over what actually runs."
        ),
        "diagram": "static/img/AIOps Framework.jpg",
        "result": [
            {"metric": "4x", "label": "Faster MTTR via AI-assisted anomaly triage, noise reduction, and root-cause analysis"},
            {"metric": "2x", "label": "Faster throughput on change request execution, through an automated deployment plan review process"},
            {"metric": "IDR 79B+", "label": "Annual revenue loss prevented via automated failover, avoiding recurrent outage incidents"},
            {"metric": "20%", "label": "Weekly engineering time reclaimed (1 day saved per 5-day week) through automated report generation"},
        ],
    },
    {
        "name": "YAML-based Terraform Standardization",
        "tagline": (
            "Replacing manual console changes with a single, YAML-configured Terraform codebase, "
            "standardizing infrastructure provisioning across a three-branch dev, staging, and "
            "production GitOps flow enforced by Terraform Enterprise."
        ),
        "role": "Associated with PT HM Sampoerna Tbk.",
        "challenge": (
            "Global compliance mandated provisioning through Terraform Enterprise's GitOps flow: "
            "a single repository with three branches for dev, staging, and production. Migrating "
            "the signature B2B workload, the company's main revenue application, meant inheriting "
            "years of unstandardized resources from earlier, less mature provisioning practices: "
            "inconsistent naming conventions and stateful or hard-to-replace resources such as IAM "
            "roles and policies, KMS encryption keys, and production databases, where an "
            "unintended destroy-and-recreate cycle risked data loss or downtime. Terraform's "
            "default behavior treats configuration drift as a trigger to replace a resource, which "
            "directly conflicted with a zero-downtime requirement from the business. Compounding "
            "this, resource existence itself was inconsistent across environments: some resources "
            "existed in dev and staging but not production, others only in one environment, a "
            "byproduct of ad hoc provisioning from before the migration began."
        ),
        "action": (
            "Rather than hand-writing Terraform per environment, which would have meant three "
            "times the code and three times the drift risk, we built a config-based approach: a "
            "single Terraform codebase driven by per-environment YAML configuration, with each "
            "resource looped over via `for_each` and filtered by a dedicated environment flag. "
            "Terraform Enterprise injects the active workspace's environment as a `TF_VAR_env` "
            "variable per its standard variable convention, which the codebase reads as `var.env` "
            "to filter which resources apply. A dev-only resource is simply skipped once code "
            "promotes to staging, no code change required. The Terraform code itself only had to "
            "be written once, and a routine change never touches a `.tf` file, only the YAML "
            "configuration, cutting the chance of accidental breakage."
        ),
        "code_samples": [
            {
                "filename": "config.yaml [SAMPLE]",
                "language": "yaml",
                "code": (
                    "buckets:\n"
                    "  app-logs:\n"
                    "    envs: [\"dev\", \"staging\", \"prod\"]\n"
                    "    versioning: true\n"
                    "  legacy-cache:\n"
                    "    envs: [\"staging\", \"prod\"]\n"
                    "    versioning: false\n"
                    "  scratch-dev-only:\n"
                    "    envs: [\"dev\"]\n"
                    "    force_destroy: true"
                ),
            },
            {
                "filename": "main.tf [SAMPLE]",
                "language": "hcl",
                "code": (
                    "variable \"env\" {\n"
                    "  type        = string\n"
                    "  description = \"Target environment, injected by Terraform Enterprise as TF_VAR_env per workspace\"\n"
                    "}\n\n"
                    "locals {\n"
                    "  config = yamldecode(file(\"${path.module}/config.yaml\"))\n\n"
                    "  buckets = {\n"
                    "    for name, cfg in local.config.buckets :\n"
                    "    name => cfg if contains(cfg.envs, var.env)\n"
                    "  }\n"
                    "}\n\n"
                    "resource \"aws_s3_bucket\" \"this\" {\n"
                    "  for_each = local.buckets\n\n"
                    "  bucket        = \"${each.key}-${var.env}\"\n"
                    "  force_destroy = try(each.value.force_destroy, false)\n\n"
                    "  tags = {\n"
                    "    Environment = var.env\n"
                    "  }\n"
                    "}"
                ),
            },
        ],
        "result_intro": (
            "With this approach, compliance is met without blocking the business: standardization "
            "concerns, like enforcing consistent bucket settings everywhere, can be tackled as a "
            "separate initiative instead of bundling every fix into the migration itself."
        ),
        "result": [
            "Standardizes infrastructure provisioning across all three environments",
            "Brings every resource into Terraform Enterprise GitOps compliance",
            "Removes the need for environment-specific Terraform code",
            "Avoids dependency on HCL syntax for routine changes, so even an engineer who isn't a Terraform expert can safely make edits through YAML",
        ],
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
            "Leading AIOps R&D for one of Indonesia's largest telcos, directing an engineering team "
            "across a sizeable AWS and Kubernetes footprint. Cut incident response time, prevented "
            "major revenue loss, and unified workflows into one agentic AI system."
        ),
        "stack": [
            {"category": "AI Automation", "items": ["Amazon Bedrock", "Microsoft Copilot Studio", "Azure AI Foundry", "n8n", "Power Platform", "Dify"]},
            {"category": "Cloud", "items": ["AWS"]},
            {"category": "Database", "items": ["Amazon RDS"]},
            {"category": "Operating System", "items": ["Amazon Linux"]},
            {"category": "Scripting & Languages", "items": ["Python", "Bash"]},
            {"category": "Orchestration & Containers", "items": ["Docker", "Containerd", "Kubernetes", "Amazon EKS", "Amazon ECS"]},
            {"category": "IaC & Config Management", "items": ["Terraform", "Amazon CloudFormation", "Helm", "Amazon SSM"]},
            {"category": "CI/CD", "items": ["GitLab Enterprise", "AWS CodeCommit", "GitLab Runner", "Jenkins", "Flux", "Amazon ECR"]},
            {"category": "Observability", "items": ["Grafana", "Datadog", "Amazon CloudWatch", "Fluentbit", "OpenTelemetry", "Prometheus"]},
            {"category": "ITSM & Documentation", "items": ["SharePoint"]},
            {"category": "Collaboration", "items": ["Microsoft Teams", "WhatsApp"]},
        ],
        "featured_link": True,
    },
    {
        "company": "PT HM Sampoerna Tbk.",
        "company_url": "https://www.sampoerna.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=sampoerna.com",
        "role": "Senior DevOps Engineer",
        "period": "June 2024 – December 2024",
        "narrative": (
            "Maintained SLAs for HM Sampoerna's app portfolio, leading an engineering group through "
            "a console-to-Terraform migration and standardizing legacy AWS accounts to Philip "
            "Morris International compliance. Cut SEA region cloud costs and automated daily "
            "repetitive tasks via Jenkins."
        ),
        "stack": [
            {"category": "Cloud", "items": ["AWS"]},
            {"category": "Database", "items": ["Amazon Aurora MySQL", "Amazon DocumentDB"]},
            {"category": "Operating System", "items": ["Amazon Linux"]},
            {"category": "Scripting & Languages", "items": ["Python", "Bash", "PowerShell"]},
            {"category": "Orchestration & Containers", "items": ["Docker", "Kubernetes", "Amazon ECS"]},
            {"category": "IaC & Config Management", "items": ["Terraform", "Amazon SSM"]},
            {"category": "DevSecOps", "items": ["Amazon Secrets Manager", "Vault", "OpenVPN", "Soteri", "Polaris", "Trivy", "Jfrog Xray", "Sonarqube", "Invicti", "Brinqa"]},
            {"category": "CI/CD", "items": ["Bitbucket", "Jenkins", "CloudBees CI", "Amazon ECR", "Jfrog Artifactory"]},
            {"category": "Observability", "items": ["Grafana", "Elastic", "Amazon CloudWatch", "New Relic", "PagerDuty", "OpsGenie"]},
            {"category": "ITSM & Documentation", "items": ["Confluence", "SharePoint", "ServiceNow"]},
            {"category": "Collaboration", "items": ["Microsoft Teams"]},
        ],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=www.telkom.co.id",
        "role": "DevOps Lead",
        "period": "April 2022 – May 2024",
        "narrative": (
            "Promoted to lead a DevOps team for Telkom's Netmonk suite, architecting a multi-tenant "
            "AWS ECS platform off legacy virtual machine deployments. Migrated Singapore to Jakarta "
            "for major cost savings, and sped up deployments via Bitbucket CI/CD."
        ),
        "stack": [
            {"category": "Cloud", "items": ["AWS", "Digital Ocean"]},
            {"category": "Database", "items": ["Aiven", "MongoDB Atlas", "Amazon RDS", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Kafka", "OpenSearch"]},
            {"category": "Operating System", "items": ["Ubuntu", "Amazon Linux", "Windows Server"]},
            {"category": "Scripting & Languages", "items": ["Python", "Bash", "Go"]},
            {"category": "Orchestration & Containers", "items": ["Docker", "Kubernetes", "Amazon ECS", "Amazon EKS"]},
            {"category": "IaC & Config Management", "items": ["Terraform", "Ansible", "Consul", "AWS Systems Manager"]},
            {"category": "DevSecOps", "items": ["Vault", "Teleport", "Nuclei", "git-secrets", "Dependency Check", "Snyk", "Trivy", "Sonarqube", "OWASP ZAP", "Nikto", "Faraday", "DefectDojo"]},
            {"category": "CI/CD", "items": ["Bitbucket", "GitLab", "Bitbucket Pipeline", "Jenkins", "Dockerhub"]},
            {"category": "Observability", "items": ["Grafana", "Datadog"]},
            {"category": "ITSM & Documentation", "items": ["Confluence", "Notion", "Jira"]},
            {"category": "Collaboration", "items": ["Slack", "Discord"]},
        ],
    },
    {
        "company": "PT Telkom Indonesia Tbk",
        "company_url": "https://www.telkom.co.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=www.telkom.co.id",
        "role": "Technical Support Engineer",
        "period": "August 2020 – April 2022",
        "narrative": (
            "Supported Netmonk clients from small businesses to large enterprises with installs, "
            "configuration, and troubleshooting. Built Terraform/Ansible pipelines that sped up "
            "deployments, and Grafana observability that improved incident response."
        ),
        "stack": [
            {"category": "Cloud", "items": ["AWS"]},
            {"category": "Operating System", "items": ["Ubuntu", "Windows Server"]},
            {"category": "Observability", "items": ["Grafana"]},
            {"category": "ITSM & Documentation", "items": ["Jira", "Trello"]},
            {"category": "Collaboration", "items": ["Slack"]},
        ],
    },
    {
        "company": "BRIN — Aviation Technology Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "System Administrator",
        "period": "June 2020 – August 2020",
        "narrative": (
            "Built an HPC lab from scratch for BRIN's Aviation Technology Research Center, planning "
            "network topology, repairing broken nodes to avoid new hardware spend, and automating "
            "OS install and configuration across the cluster."
        ),
        "stack": [
            {"category": "Operating System", "items": ["CentOS", "Ubuntu", "Windows 10"]},
            {"category": "IaC & Config Management", "items": ["Kickstart", "C3 (Cluster Control)"]},
            {"category": "Networking & Hardware", "items": ["Supermicro", "Cisco Switch", "LAN", "WLAN"]},
        ],
    },
    {
        "company": "BRIN — Informatics Research Center",
        "company_url": "https://www.brin.go.id",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=brin.go.id",
        "role": "Junior System Administrator",
        "period": "February 2019 – December 2019",
        "narrative": (
            "Helped maintain an HPC lab at BRIN's Informatics Research Center, repairing damaged "
            "nodes, automating new node installs, and rolling out Puppet configuration management "
            "for consistent infrastructure state."
        ),
        "stack": [
            {"category": "Operating System", "items": ["CentOS", "Ubuntu", "Windows Hyper-V"]},
            {"category": "IaC & Config Management", "items": ["Puppet", "Kickstart", "C3 (Cluster Control)", "Foreman"]},
            {"category": "Networking & Hardware", "items": ["Cisco Switch", "Aruba Switch", "MikroTik", "LAN", "WLAN"]},
        ],
    },
    {
        "company": "PT Griya Mitra Persada",
        "company_url": "https://www.griyamitrapersada.com",
        "company_logo": "https://www.google.com/s2/favicons?sz=128&domain=griyamitrapersada.com",
        "role": "IT Support Lead",
        "period": "July 2018 – September 2018",
        "narrative": (
            "Led an on-site IT support team across end-devices at Pakansari Stadium during the "
            "Asian Games, installing, testing, and auditing devices to keep every match running "
            "smoothly."
        ),
        "stack": [
            {"category": "Operating System", "items": ["Windows 10", "Windows 7"]},
            {"category": "Networking & Hardware", "items": ["Canon Printers", "HP Printers & Copiers", "HP Laptops & AIO PCs", "TP-Link Access Point", "LAN", "WLAN"]},
        ],
    },
]

EDUCATION = [
    {"school": "UIN Syarif Hidayatullah Jakarta", "degree": "Bachelor of Computer Science", "year": "2023"},
    {"school": "SMKN 3 Bogor", "degree": "Vocational Diploma in Computer Networks", "year": "2016"},
]
