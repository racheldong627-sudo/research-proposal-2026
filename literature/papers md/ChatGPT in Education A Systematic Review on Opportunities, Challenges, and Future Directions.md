# Literature Review: ChatGPT in Education A Systematic Review on Opportunities, Challenges, and Future Directions

**Source:** `papers pdf/ChatGPT in Education A Systematic Review on Opportunities, Challenges, and Future Directions.pdf`  
**Converted:** 2025-11-05 15:15:37  
**Status:** Auto-converted from PDF using PyMuPDF  

---



## Page 1

Academic Editors: Frank Werner,
Antonio Sarasa Cabezuelo and María
Estefanía Avilés Mariño
Received: 25 April 2025
Revised: 25 May 2025
Accepted: 2 June 2025
Published: 6 June 2025
Citation:
Munaye, Y.Y.; Admass, W.;
Belayneh, Y.; Molla, A.; Asmare, M.
ChatGPT in Education: A Systematic
Review on Opportunities, Challenges,
and Future Directions. Algorithms
2025, 18, 352. https://doi.org/
10.3390/a18060352
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
algorithms
Systematic Review
ChatGPT in Education: A Systematic Review on Opportunities,
Challenges, and Future Directions
Yirga Yayeh Munaye 1,*
, Wasyihun Admass 2
, Yenework Belayneh 1, Atinkut Molla 1
and Mekete Asmare 3
1
Department of Information Technology, Injibara University, Injibara P.O. Box 40, Ethiopia;
yenework.belayneh@inu.edu.et (Y.B.); atinkut.molla@inu.edu.et (A.M.)
2
School of Software Engineering, University of Science and Technology of China, Suzhou 215123, China;
bywasyihun@gmail.com
3
Department of Electrical and Computer Engineering, Injibara University, Injibara P.O. Box 40, Ethiopia;
mekete.asmare@inu.edu.et
*
Correspondence: byyirga@gmail.com
Abstract: This study presents a systematic review on the integration of ChatGPT in educa-
tion, examining its opportunities, challenges and future directions. Utilizing the PRISMA
framework, the review analyzes 40 peer-reviewed studies published from 2020 to 2024.
Opportunities identified include the potential for ChatGPT to foster individualized educa-
tional experiences, tailoring learning to meet the needs of individual students. Its capacity
to automate grading and assessments is noted as a time-saving measure for educators,
allowing them to focus on more interactive and engaging teaching methods. However, the
study also addresses significant challenges associated with utilizing ChatGPT in educa-
tional contexts. Concerns regarding academic integrity are paramount, as students might
misuse ChatGPT for cheating or plagiarism. Additionally, issues such as ChatGPT bias
are highlighted, raising questions about the fairness and inclusivity of ChatGPT-generated
content in educational materials. The necessity for ethical governance is emphasized,
underscoring the importance of establishing clear policies to guide the responsible use
of AI in education. The findings highlight several key trends regarding ChatGPT’s role
in enhancing personalized learning, automating assessments, and providing support to
educators. The review concludes by stressing the importance of identifying best practices
to optimize ChatGPT’s effectiveness in teaching and learning environments. There is a clear
need for future research focusing on adaptive ChatGPT regulation, which will be essential
as educational stakeholders seek to understand and manage the long-term impacts of
ChatGPT integration on pedagogy.
Keywords: ChatGPT in education; artificial intelligence; AI in pedagogy; AI-powered
learning
1. Introduction
The rapid advancement of artificial intelligence (AI) has significantly transformed
various sectors, including education. Among AI-driven tools, chat generative pre-trained
transformer (ChatGPT), developed by OpenAI, has gained prominence due to its ability to
generate human-like text, assist in tutoring, content creation, and interactive discussions,
and support students and educators in diverse learning environments [1] with significant
benefits, including personalized learning, automated assessments, and administrative
efficiency. However, its integration into education also raises concerns regarding academic
integrity, data privacy, AI biases, and its long-term impact on pedagogy [2].
Algorithms 2025, 18, 352
https://doi.org/10.3390/a18060352


## Page 2

Algorithms 2025, 18, 352
2 of 28
Although the governance and ethical implications of ChatGPT in education remain
underexplored [3], some researchers argue that AI could enhance critical thinking and
engagement, while others warn of plagiarism risks, misinformation, and the erosion of
teacher authority [4]. Additionally, disparities exist in institutional AI consistency in its use
across educational settings [5]. To address these complexities, this study conducts a system-
atic review using the preferred reporting items for systematic reviews and meta-analyses
(PRISMA) framework, evaluating ChatGPT’s role in teaching, learning, governance, and
policy challenges. By analyzing both its opportunities and risks, the study provides insights
into best practices for responsible AI integration in education.
Despite its transformative potential, the integration of ChatGPT in education presents
several critical challenges that require urgent attention. One of the most pressing concerns is
that students increasingly rely on ChatGPT for assignments and assessments, raising risks
of plagiarism and reduced critical thinking skills [6]. Educational institutions must establish
clear guidelines to ensure AI is utilized as a learning aid rather than a substitute for inde-
pendent intellectual engagement [7]. Another major challenge is bias and misinformation in
AI-generated content. Since ChatGPT is trained on vast datasets, it can sometimes produce
inaccurate, misleading, or biased responses, which may reinforce harmful stereotypes and
misinform students [8]. To mitigate this risk, continuous refinement of AI models and AI
literacy programs is necessary, equipping students with critical evaluation skills when
engaging with AI-generated content [9]. Additionally, privacy and ethical concerns sur-
rounding AI adoption in education remain significant. ChatGPT processes large amounts of
user data, raising concerns about data security, student privacy, and compliance with regula-
tory frameworks [10]. However, the absence of standardized AI governance policies further
complicates responsible AI integration in educational settings [11]. Addressing these issues
requires the development of robust ethical guidelines and governance structures to ensure
the safe, transparent, and equitable use of AI in education.
Furthermore, educators face difficulties in adapting to AI-driven teaching method-
ologies. While AI can automate administrative tasks, its effective classroom integration
demands teacher training and institutional support. Without proper training, educators
may struggle to leverage AI while maintaining pedagogical effectiveness. Research must
explore how AI literacy and professional development programs can empower educators
to maximize AI’s benefits while mitigating its risks [12,13]. Moreover, to address these
complexities, this study explores the following research questions:
(1)
How has ChatGPT been applied in education?
(2)
What are the major governance and policy challenges associated with its adoption?
(3)
What future research directions can optimize its effectiveness while ensuring ethi-
cal implementation?
By investigating these questions, this study aims to provide a comprehensive analysis
of ChatGPT’s role in education, offering insights into its applications, challenges, and
future implications. The findings will contribute to ongoing discussions on responsible AI
adoption in academic settings, guiding educators, policymakers, and researchers toward
effective and ethical AI integration. Therefore, the main contributions of this work are
summarized as follows:
(1)
Comprehensive Analysis of ChatGPT in Education: This study presents a systematic
review of 40 peer-reviewed studies (2020–2024) using the PRISMA framework, of-
fering a structured and evidence-based understanding of ChatGPT’s applications in
educational settings.
(2)
Identification of Opportunities for Educational Enhancement: The review highlights
how ChatGPT can personalize learning, automate grading, and support educators,
displaying its potential to enhance student engagement and optimize teaching efficiency.


## Page 3

Algorithms 2025, 18, 352
3 of 28
(3)
Critical Examination of Challenges: It addresses major concerns such as academic
integrity, AI bias, and the lack of inclusivity, contributing to a balanced understanding
of both the benefits and risks of integrating ChatGPT into education.
(4)
Call for Ethical Governance and Future Research: The study emphasizes the need for
ethical policy frameworks and future research on adaptive regulation and long-term
pedagogical impact, guiding stakeholders in responsible AI adoption in education.
Finally, this paper is organized as follows: Section 1 provides an overview of ChatGPT,
Section 2 discusses its applications in education, Section 3 outlines the systematic review
methodology, Section 4 explores the identified opportunities and future directions, and
Section 5 presents the conclusion along with recommendations for future research.
2. Methods and Materials
2.1. Inclusion and Exclusion Criteria
2.1.1. Inclusion
Peer-reviewed journal articles, conference papers, and empirical studies focusing
on ChatGPT’s role in education and its governance were included. Studies on broader
AI-related challenges in education, even if they do not focus exclusively on ChatGPT, were
also included as shown in Table 1.
Table 1. Summary of inclusion and exclusion criteria.
Stage
Number of Studies
Criteria Applied
Identification
150
Initial search results from databases
Duplicate removal
20
Studies appearing multiple times
in searches
Screening
130
Title and abstract reviewed
for relevance
Exclusion (Abstract)
50
Not related to ChatGPT, general AI
topics only
Full-Text Assessment
80
Studies with relevant research scope
Exclusion (Full-Text)
40
Missing methods, weak evidence,
outdated sources
Final Inclusion
40
Studies that met all inclusion criteria
2.1.2. Exclusion
Non-peer-reviewed articles, opinion pieces, and studies lacking empirical validation
were excluded. Additionally, we reviewed research considering ethics, collaboration, and
policy development in AI education, taking inspiration on systematic AI in education.
This study employs a systematic approach to reviewing the literature on the appli-
cations, potential, and challenges associated with ChatGPT in education. As shown in
Figure 1, 40 papers were chosen from an initial pool of 150 studies gathered between 2020
and 2024 using Scopus, Web of Science, IEEE Xplore, Google Scholar, and Springer Link.
The compilation of data from these 40 publications yielded 10 primary themes, including
15 benefits, 15 drawbacks and various opportunities and problems linked with ChatGPT’s
integration into teaching and learning.


## Page 4

Algorithms 2025, 18, 352
4 of 28
Figure 1. Collection of articles using the PRISMA paradigm.
2.2. Source of Information
To ensure comprehensive literature coverage, multiple databases were used. The
selected databases include Scopus, Web of Science, IEEE Xplore, Google Scholar, and
Springer Link, which contain a wealth of peer-reviewed academic articles relevant to AI in
education. This multi-database approach enhances the reliability and depth of the literature
review as illustrated in Table 2.
Table 2. Criteria for paper selection.
Phase
Criteria
Papers
Identified
Explanation for Search and
Identification
Search and
Identification
Use of multiple databases (Scopus, Web
of Science, IEEE Xplore, Google Scholar,
and Springer Link) with relevant
keywords and Boolean operators
150
Initial search across selected databases
targeting ChatGPT applications,
opportunities, and challenges
in education.
Screening
Studies published between 2020 and
2024, written in English, and
peer-reviewed
120
Abstract screening and relevance check
to ensure alignment with research focus.


## Page 5

Algorithms 2025, 18, 352
5 of 28
Table 2. Cont.
Phase
Criteria
Papers
Identified
Explanation for Search and
Identification
Eligibility
Studies specifically discussing
ChatGPT’s applications, opportunities,
and challenges in education
50
Detailed review of abstracts to filter
studies most relevant to the research
questions.
Inclusion
Studies with empirical data, theoretical
discussions, and case studies on
ChatGPT in education
40
Full-text review and thematic coding to
finalize included studies.
2.3. Search Process
A systematic search strategy was employed to identify relevant research. This approach
resulted in the collection of 150 papers using specific search strings targeting ChatGPT’s
applications, opportunities, and challenges in education. The search process involved
•
Defining relevant keywords related to ChatGPT’s role in education;
•
Applying Boolean operators (e.g., AND, OR) to refine search queries;
•
Implementing inclusion and exclusion criteria to filter the most relevant studies;
•
Using reference management software to organize and manage selected articles.
2.4. Paper Selection Criteria
The study adhered to the PRISMA guidelines. The selection criteria included:
•
Timeframe: Studies published between 2020 and 2024;
•
Language: Only studies published in English were considered;
•
Publication Type: Peer-reviewed journal articles and conference papers;
•
Relevance: Articles focused on the applications, opportunities, and challenges of
ChatGPT in education.
2.5. Selection Process
A multi-stage selection process was employed to filter the most relevant papers:
•
Initial Screening: Abstracts were reviewed to assess relevance. Only studies discussing
ChatGPT’s role in education were considered.
•
Full-Text Review: The selected papers (40 articles) were read in full to evaluate their
contribution to the research questions.
•
Coding Process: The review papers were analyzed using grounded theory coding,
which included
◦
Open Coding: Identifying key research themes, opportunities, and challenges.
◦
Axial Coding: Categorizing themes into broader topics.
◦
Selective Coding: Synthesizing the most critical findings.
2.6. PRISMA Flowchart
The selection process for this systematic review follows the PRISMA guidelines, as
illustrated in the flowchart in Figure 1. This study systematically selected and reviewed
research papers published from 2020 to 2024. The data included search terms such as Chat-
GPT in education, ChatGPT opportunities, ChatGPT governance in education, ChatGPT
and teacher workload, and ethical concerns in ChatGPT-driven education.
2.7. Distribution of Articles Used in Systematic Review
The majority of relevant studies were published between 2023 and 2024, reflecting
the growing interest in ChatGPT’s role in education. These findings align with related


## Page 6

Algorithms 2025, 18, 352
6 of 28
works, emphasizing recent AI advancements and their educational implications. This study
follows a systematic review approach to analyze the applications, benefits, challenges, and
future directions of ChatGPT in education. As illustrated in Figure 1, 150 studies published
between 2020 and 2024 were initially collected. After applying inclusion and exclusion
criteria, 40 relevant papers were selected for in-depth analysis. Furthermore, Figure 2
presents the distribution of selected papers by publication year, highlighting the percentage
of studies included in our systematic review. This visualization provides insights into the
temporal trends in research on the topic, highlighting the evolution of scholarly interest
and contributions over time. This shows that over 90% of the references are from 2023 and
2024, indicating that this study is supported by recent and relevant research.
 
Figure 2. Yearly published articles used for systematic review in percent.
Moreover, as illustrated in Figure 3, an extensive search was conducted across multiple
academic databases to identify relevant articles for our systematic review. Various databases
were explored to ensure comprehensive coverage of the topic, and the selection of the most
relevant sources is highlighted in the figure. This rigorous search strategy aimed to include
high-quality, peer-reviewed studies that contribute valuable insights to our research.


## Page 7

Algorithms 2025, 18, 352
7 of 28
 
Figure 3. Selected databases for paper selection.
3. Related Works
Table 3 is a key component of our study, providing a systematic overview of the
selected sample and relevant articles reviewed. This table includes essential details such as
the reference list, year of publication, models employed, datasets utilized, methodological
approaches, performance metrics, study objectives, key findings, strengths, and limitations
of each study. By systematically organizing this information, Table 3 facilitates a clearer
understanding of existing research, enabling comparisons across studies and identifying
research gaps that our work aims to address.
Table 3. Summary of related articles reviewed.
Ref.
Year
Methods
Dataset
Findings
Limitations
[1]
2024
SWOT
Analysis
Not specified
ChatGPT uses a sophisticated natural
language model to generate plausible
answers, with self-improving capability,
and provides personalized and real-time
responses. Increases access to information,
facilitates complex learning, and decreases
teaching workload.
Lack of deep understanding,
difficulty in evaluating the quality
of responses, a risk of bias and
discrimination, and lack of
higher-order thinking skills.
[2]
2023
Descriptive
Analysis
Not specified
ChatGPT, as a language processing tool,
can answer user questions, complete tasks,
and continuously optimize performance. It
holds great potential for promoting
educational transformation and school
education reform.
Issues include the accuracy of
answering questions, data
pollution, ethical and safety
concerns, and the risk of
knowledge plagiarism.


## Page 8

Algorithms 2025, 18, 352
8 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[3]
2024
Empirical
Study
30 theory-
based and
application-
based ChatGPT
tests
ChatGPT provides a platform for
students to seek answers to theory-based
questions and generate ideas for
application-based questions and allows
instructors to integrate technology in
classrooms. It can replace search engines
by providing accurate and reliable input
to students.
ChatGPT may lead to unethical
use by students, contributing to
human unintelligence and
unlearning. It presents challenges
for instructors in differentiating
between students who rely on
automation and those who do not,
and measuring learning outcomes.
[4]
2024
Online
Survey
201 HE students
in Peru
Perceived Ethics (B = 0.856) and Student
Concerns (B = 0.802). Findings suggest
that students’ knowledge and positive
attitudes toward ChatGPT do not
guarantee its effective adoption and use.
The dependence on ChatGPT raises
ethical concerns.
No differences found between sex
and age in the relationship
between the use of ChatGPT and
perceived ethics. Further studies
with diverse HE samples needed.
[5]
2023
Literature
Review
Not specified
ChatGPT has demonstrated remarkable
proficiency, including passing the US bar
law exam, and quickly gained over a
million subscribers. It can generate
humanlike text and facilitate
automated conversations.
Mixed reactions in
education—some educators view
it as a progressive step, while
others are concerned it may reduce
analytical skills and promote
misconduct. Concerns regarding
its widespread use and opacity
remain within the
scientific community.
[6]
2023
Ethical
Reflection
and Argu-
mentation
Personal
experience,
academic policy
review
The paper presents a perspective on how
students could defend their use of
ChatGPT in academic settings, arguing
that AI is a tool and not a person, and
thus does not require attribution. The
author suggests that the use of AI like
ChatGPT might not constitute cheating or
plagiarism, as long as the process aligns
with educational goals and standards.
The need for universities to adjust
academic dishonesty definitions to
address AI use, but also to avoid
automatic reactions like banning AI.
The author suggests that defining
cheating to include AI use only
when prohibited by the instructor
would offer more flexibility.
However, a change in academic
policy might not universally resolve
ethical concerns.
[7]
2024
Systematic
Literature
Review (SLR)
44 peer-
reviewed
articles
ChatGPT can assist with teaching
support, task automation, and
professional development. Student Uses:
24/7 support, explaining difficult
concepts, acting as a conversational
partner, providing personalized feedback
and materials, offering writing support,
self-assessment, facilitating engagement,
and promoting self-determination.
Inaccuracies and hallucinations,
potential bias, tool limitations,
plagiarism, cheating, privacy
issues, and the spread of false
information. These issues
highlight the challenges of using
ChatGPT effectively in education.
[8]
2023
Case Study
(Activity-
based)
Georgia
Gwinnett
College (GGC)
students in
introductory
chemistry
courses
ChatGPT-based activity led to
improvements in students’ confidence to
ask insightful questions, analyze
information, and comprehend complex
concepts. Students reported that
ChatGPT provided diverse perspectives
and challenged their current thinking.
They were also willing to recommend it
to others.
Low-quality student comments,
difficulties in validating
information sources.


## Page 9

Algorithms 2025, 18, 352
9 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[9]
2024
Qualitative
Evaluation
Insights from
leading
academics,
scientists, and
engineers
ChatGPT can help educators by creating
instructional content, offering
suggestions, acting as an online
educator, and promoting group work. It
performs differently across subjects
(finance, coding, math, general queries)
and can transform education through
smartphones and IoT gadgets.
Possibility of producing inaccurate
or false data, circumventing
plagiarism detectors, and incorrect
outputs, which limit its overall
benefit in some
educational contexts.
[10]
2024
SLR
51 articles from
Scopus, ERIC,
Google Scholar
(2022–2023)
Data extracted from 51 studies revealed
32 topics including 13 strengths,
10 weaknesses, 5 opportunities, and
4 threats of using ChatGPT in teaching
and learning. The study applied Biggs’s
Presage–Process–Product (3P) model to
categorize these topics. The results
highlight how ChatGPT interacts with
student characteristics and teaching
contexts, how it affects teaching and
learning activities, and how it
contributes to student
learning outcomes.
The study does not mention
specific limitations, but as a
systematic review, it may have
limitations in terms of the quality
and scope of selected studies. The
included articles’ methodologies
and focus areas could influence the
synthesis of data.
[11]
2023
SLR
PubMed, IEEE
Xplore, Google
Scholar (peer-
reviewed articles,
prominent media
outlets, English
publications)
AI chatbots like ChatGPT have potential
benefits in Higher Education Institutions
(HEIs), such as research support,
automated grading, and improved
human–computer interaction. It also
offers applications in enrollment, student
services, teaching enhancements,
research aid, and student retention.
However, risks include plagiarism,
online testing security concerns, privacy
breaches, misuse, bias, and decreased
human interaction.
Incomplete representation of AI’s
overall effect on education, lack of
concrete guidelines for integration,
and focus only on selected
peer-reviewed and
media-based sources.
[12]
2023
Comprehen-
sive Review
Literature
review on
ChatGPT and its
applications in
various
industries
ChatGPT has applications in customer
service, healthcare, education, and
scientific research. It aids in data
processing, hypothesis generation,
collaboration, and public outreach. The
study also highlights critical challenges,
including ethical concerns, data biases,
safety issues, and the need for
integration with other technologies.
ChatGPT has gained significant
attention from academia, research,
and industries.
Ethical concerns, data biases, and
safety issues related to ChatGPT’s
use. Challenges in balancing
AI-assisted innovation with
human expertise. Potential biases
in AI and limitations in current
understanding of its impact.
[13]
2023
Commentary
Not Shown
The launch of ChatGPT has sparked
concerns regarding student assessment.
GAI systems can benefit students, faculty,
and administrators in teaching, learning,
research, and professional activities. The
article explores potential benefits and
risks, including equity and
accessibility concerns.
Potential challenges regarding
assessment and ethical issues in the
use of GAI systems. Equity and
accessibility concerns need to be
addressed.


## Page 10

Algorithms 2025, 18, 352
10 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[14]
2023
Review and
Commentary
Not Shown
LLMs like ChatGPT have significant
potential to enhance education by
improving grading, feedback, language
learning, and personalized instruction.
However, they also raise ethical
concerns like bias, academic integrity
issues (e.g., plagiarism), and lack of
transparency in the underlying models.
Academic institutions have had varying
responses, with some banning and
others encouraging LLM usage.
Ethical concerns (e.g., bias,
plagiarism), lack of transparency in
LLM models, and challenges in
detecting AI-generated content. AI
systems lack human interaction and
cannot fully understand or
contextualize information, limiting
their effectiveness.
[15]
2023
Pre-test and
online survey
225 responses
from primary
and secondary
education
teachers
Perceived ease of use and perceived
usefulness lead to greater acceptance of
chatbots. Teachers are more likely to
accept chatbots with formal language.
Results provide insights into chatbot
design and communication decisions to
enhance acceptance in the
educational community.
Limited to primary and secondary
education teachers; does not
account for other factors
influencing chatbots acceptance
beyond age and digital skills.
[16]
2023
Analysis of
course
evaluation
data
Physical
Chemistry I and
II courses at two
institutions
Students had a positive response to oral
exams, finding them valuable despite
challenges like stress, anxiety, and the
depth of understanding required.
Students adjusted study habits
(e.g., group study, verbal practice) and
recognized the value of communication
and teamwork for their future careers.
Instructors valued oral exams, though
concerns about time commitment,
validity, reliability, and
fairness persisted.
Study focused on two institutions,
limited to Physical Chemistry
courses; concerns about time,
validity, reliability, and fairness
were not fully resolved.
[17]
2024
Narrative
review and
qualitative
synthesis
40 peer-
reviewed
empirical
studies
The adoption of ChatGPT in higher
education is influenced by factors such as
hedonic motivation, usability, perceived
benefits, system responsiveness, and
relative advantage. Social influence,
facilitating conditions, privacy, and
security have varying effects. Technology
readiness and extrinsic motivation not
consistently confirmed as predictors. The
study highlights the need for deeper
exploration of contextual and
psychological factors.
The review primarily synthesizes
empirical studies and does not
provide new primary data. It
focuses on higher education,
which may not be generalizable to
other sectors.
[18]
2023
Study and
evaluation of
ChatGPT-
generated
responses
Two chemistry-
focused
modules in a
pharmaceutical
science program
(Year 1 and
Year 2)
ChatGPT-generated responses were
successful for knowledge-based
questions (e.g., “describe” and “discuss”
verbs) but faced limitations in
answering application-based and
interpretation questions involving no
text information. ChatGPT not
considered a high-risk tool for cheating
but expected to prompt discussions on
academic integrity and assessment
design in education.
The study focuses on specific
chemistry modules in a
pharmaceutical science program,
which may not generalize to other
disciplines. Further, it primarily
evaluates response quality without
exploring broader applications or
potential consequences.


## Page 11

Algorithms 2025, 18, 352
11 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[19]
2020
SLR and
meta-
analysis
Various studies
related to
environmental
science and
ecosystem
services
The paper introduces the PSALSAR
method, an enhanced version of the
traditional SALSA framework for
conducting systematic literature reviews
(SLRs) and meta-analysis. This method
includes six steps: Protocol, Search,
Appraisal, Synthesis, Analysis, and
Reporting. It is transferable,
reproducible, and applicable for
assessing both quantitative and
qualitative content in literature reviews,
particularly in ecosystem services.
The methodology focuses on
environmental science and
ecosystem services, limiting its
application to other disciplines. It
is not clear if the methodology
addresses challenges in broader or
interdisciplinary fields.
[20]
2023
Literature
review and
thematic
analysis
1 papers from
the “Computers
& Education:
Artificial
Intelligence”
Special Issue
The Special Issue discusses seven main
themes regarding the integration of AI in
education: (1) intersection between AI and
humans, (2) challenges and opportunities
in AI for assessment, (3) explainability of
AI, (4) design principles for AI-driven
systems, (5) development of new theories
of learning, (6) predictions and their role in
education, and (7) AI applications in
classrooms. It emphasizes challenges like
ethics, bias, AI literacy, data sources, and
policy development.
The studies may focus more on
theoretical frameworks and policy
discussions rather than providing
concrete, actionable insights or
empirical data on AI’s practical
implementation in diverse
educational contexts.
[21]
2023
Commentary
and opinion
piece
Discussions in
academic
settings and
media
ChatGPT has gained significant attention
in academia due to its ability to assist in
academic writing. Concerns exist
regarding academic integrity, as students
may misuse the tool for cheating.
However, tools like Turnitin are
developed to counteract such cheating.
Despite risks, AI will be integrated into
higher education with new policies and
adaptation strategies. The academic
community remains resilient, much like
past technological adaptations
(e.g., computer use in teaching).
The discussion primarily presents
speculative views on the future of
AI in academia without offering
conclusive evidence or studies to
support the opinions. Additionally,
it does not delve deeply into the
full range of potential ethical
issues or institutional responses.
[22]
2023
Narrative
literature
review and
SWOT
analysis
Scholarly
articles and
reports on
ChatGPT
integration in
nursing
education
The review identifies strengths
(accessibility, consistency, adaptability,
cost-effectiveness, staying up-to-date),
weaknesses, opportunities, and threats
associated with ChatGPT in nursing
education. It emphasizes the need for
responsible use and collaboration among
educators, policymakers, and AI
developers to enhance learning outcomes.
The study only provides a SWOT
analysis and literature review,
without empirical data or direct case
studies to validate the integration of
ChatGPT in real-world nursing
education contexts.
[23]
2022
Conceptual
paper with a
review of AI
applications
in education
Educational
resources from
MIT Media Lab
and Code.org
The paper identifies the potential benefits
of AI in K-12 education, such as
personalized learning, automated
assessments, and behavioral insights. It
also highlights the ethical challenges of
AI in education, emphasizing the need
for ethical considerations in integrating
AI. Recommendations for instructional
resources provided to help educators
teach AI concepts and ethics.
The paper does not provide
empirical data or case studies on
the real-world implementation of
AI in K-12 classrooms. It primarily
focuses on theoretical concepts
and ethical considerations.


## Page 12

Algorithms 2025, 18, 352
12 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[24]
2023
Narrative
review,
thematic
analysis
40 peer-
reviewed
empirical
studies
The review identifies key factors
influencing ChatGPT adoption in higher
education, including hedonic motivation,
usability, perceived benefits, and system
responsiveness. It emphasizes the need
for deeper exploration of contextual and
psychological factors beyond traditional
technology adoption models.
The review focuses on existing
literature, and its findings based
on qualitative synthesis. It does
not present new empirical data or
experimental findings.
[25]
2023
Literature
review,
historical
analysis
Open AI’s
ChatGPT, the
literature on AI
history and uses
in education
The paper outlines the rapid success of
ChatGPT and generative AI (GAI)
technologies, examining their advantages
and disadvantages, particularly regarding
human agency versus machine agency. It
discusses strategies to avoid current
problems and emphasizes how humans
can maintain autonomy while using GAI.
The paper proposes revised “Laws of
Generative Artificial Intelligence” to guide
education in the GAI era.
The paper does not provide new
empirical data but offers a
conceptual and historical analysis,
which may limit its applicability to
practical scenarios without
further research.
[26]
2023
SLR
Multiple journal
databases,
filtered by
specific criteria
ChatGPT has the potential to enhance
both academic and librarian-related
processes in higher education. However,
it raises ethical concerns and challenges
related to critical thinking development.
The study highlights the importance of
the responsible use of ChatGPT and the
need for further assessment of its use in
academic contexts.
The study relies solely on existing
literature and may not capture
real-time developments or
practical applications.
Additionally, the SLR
methodology may introduce
selection biases based on
included articles.
[27]
2021
Extensive
literature
review
67 relevant
studies selected
from various
academic
databases
AI chatbots in education offer significant
benefits, such as providing homework and
study assistance, creating personalized
learning experiences, and supporting skill
development. Educators benefit from
time-saving assistance and improved
pedagogy. However, challenges such as
concerns about reliability, accuracy, and
ethical issues are highlighted.
Based on selected studies and may
not account for emerging issues or
practical applications. Limited by
the predefined criteria used for
selecting the studies.
[28]
2023
Systematic
review
53 articles from
recognized
digital
databases
The study provides a comprehensive
understanding of previous research on the
use of chatbots in education. It identifies
the benefits and challenges of chatbots
technology, as well as future research areas
for its implementation in education.
It is based on recognized databases
and could miss emerging or less
mainstream research.
[29]
2023
SLR using
the PRISMA
framework
Journal articles
from Scopus
(published in
English in the
last five years)
The review investigates the support
chatbots provide to educational
institutions and students, emphasizing
their roles as teaching assistants, their
capabilities, and usage recommendations.
It also identifies students’ desires and
challenges in chatbots use.
The review is limited to articles
published in English and available
in Scopus, using a general search
query and only focusing on the
last five years of research.
[30]
2023
Exploratory
study,
literature
synthesis
Recent literature
on ChatGPT in
education
ChatGPT promotes personalized and
interactive learning and aids in generating
formative assessment prompts with
ongoing feedback, but also generates
wrong information, biases, and privacy
issues. The study recommends leveraging
ChatGPT to maximize its benefits.
Potential drawbacks include
ChatGPT generating wrong
information, biases in data
training, and privacy concerns.


## Page 13

Algorithms 2025, 18, 352
13 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[31]
2023
Critical
analysis,
literature
review
Research on
OpenAI,
ChatGPT, and
education in
developing
economies
ChatGPT presents significant
opportunities for advancement in
education, particularly in developing
economies, but also has potential
drawbacks.
The study primarily focuses on
understanding the technology’s
impact, but may not fully capture
the real-world challenges in the
implementation of
such technologies.
[32]
2020
Theoretical
framework
(IDEE),
exploration of
benefits and
challenges
Research on
ChatGPT,
GPT-4, and
educative AI in
education
Benefits include personalized learning,
efficient feedback, and more, but
challenges include untested effectiveness,
data limitations, and ethical concerns.
Uncertainty about the effectiveness
of the technology, and
ethical/safety concerns need
further exploration.
[33]
2023
Exploratory
study,
literature
synthesis
Recent extant
literature on
ChatGPT in
education
ChatGPT promotes personalized
learning, interactive learning, and
formative assessment generation. It helps
inform teaching but has limitations like
wrong information, biases, and
privacy issues.
ChatGPT generates incorrect
information, biases in training
data, privacy concerns, and
potential bias amplification.
[34]
2024
Pilot study,
case study
approach
Three chatbot
prototypes under
development at
Warwick Manu-
facturing Group,
University of
Warwick
Chatbots show potential in educational
simulation, software training, and
helpdesk support. The prototypes aimed
to support a Master’s simulation game,
software training, and department
helpdesk requests.
Limited to university setting, and
specific focus on technical
challenges and AI chatbot
development in
educational contexts.
[35]
2024
Quantitative,
descriptive
research
143 students
from two public
universities in
Islamabad
Most students agreed on the benefits of
AI tools for academics. However,
concerns about academic integrity,
regulations, privacy, cognitive biases,
gender and diversity, accessibility, and
commercialization raised.
Focused only on students from
two universities in Islamabad,
which may limit the
generalizability of results.
[36]
2023
Quantitative
research
(survey),
Structural
Equation
Modeling
(SEM)
520 students
from a public
university in
Saudi Arabia
(SA)
Significant direct effects of performance
expectancy (PE), social influence (SI), and
effort expectancy (EE) on behavioral
intention (BI) and actual use of ChatGPT.
Partial mediation of BI between PE, SI,
FC, and actual use. Full mediation of BI
between EE and actual use. FCs had no
significant effect.
Limited to one university in Saudi
Arabia and did not consider
external resources and support for
ChatGPT use.
[37]
2023
Quantitative
research
(survey),
SEM
458 participants
(students) using
ChatGPT for
smart education
systems
Perceived ease of use and perceived
usefulness were significant predictors of
users’ attitudes towards ChatGPT.
Feedback quality, assessment quality, and
subject norms positively influenced users’
behavioral intentions. Positive attitudes
and intentions led to actual adoption.
Some hypotheses, such as the
relationship between trust in
ChatGPT and perceived
usefulness, not supported by
the data.
[38]
2023
Systematic
literature
review
(PRISMA
framework)
550 articles
(collected
between
December 2022
and May 2023),
final 30 articles
selected
ChatGPT seen as a tool with both
opportunities and challenges in academic
writing. It helps learners and instructors
but requires updated training, policies,
and assessments to address issues like
plagiarism and AI-generated content.
Limited to 30 articles selected from
550, which may not cover all
perspectives or studies; challenges
in addressing AI’s impact on
assessment methods and integrity.


## Page 14

Algorithms 2025, 18, 352
14 of 28
Table 3. Cont.
Ref.
Year
Methods
Dataset
Findings
Limitations
[39]
2024
Qualitative
study
Views of three
established
professors in
South Africa
Professors welcome the use of AI
technologies like ChatGPT and
emphasize the importance of teaching
students how to engage with such tools.
The responsibility lies with lecturers and
universities to create an environment
conducive to integrating these
technologies into teaching and learning,
especially in assessment.
Limited to the views of three
professors in South Africa; may not
represent a broader perspective.
[40]
2023
Systematic
review
36 papers on
chatbot–learner
interaction
design
Chatbots were mainly used on web
platforms, primarily teaching computer
science, language, and general education,
with some used for engineering and
mathematics. Most chatbots acted as
teaching agents, with more than a third
as peer agents. More than a quarter of
chatbots employed personalized learning
approaches. Chatbots evaluations show
improved learning and satisfaction.
Insufficient dataset training, lack
of reliance on usability heuristics,
and challenges in chatbots’
personality and localization.
4. Opportunities of ChatGPT in Education
The advancement ChatGPT technology in recent years has had a considerable impact
on a variety of fields, including research and education. ChatGPT, a powerful massive
language model developed by OpenAI, is an example of such technology. Personalized
feedback, increased accessibility, interactive discussions, lesson preparation, evaluation,
and novel approaches to teaching difficult concepts are just a few of the exciting oppor-
tunities that this technology provides for both students and teachers. Furthermore, the
incorporation of ChatGPT into education provides several chances to improve teaching and
learning experiences. AI-powered solutions such as ChatGPT provide a variety of benefits,
including individualized learning, automated content development, real-time student help,
and increased engagement.
This section delves into significant opportunities for exploiting ChatGPT for education.
However, ChatGPT poses a variety of threats to the traditional educational and research
systems, including the possibility of online exam cheating, text generation that resembles
that of a person, a reduction in critical thinking abilities, and difficulties in interpreting
data generated by ChatGPT [23]. According to [24], ChatGPT is used as a teaching and
learning tool. Additionally, instructors and students enrolled in composition, business
writing, and communication courses can use ChatGPT’s features. It also used to provide
recommendations. Moreover, ChatGPT is applicable in the classroom [25] to students,
who can build study materials and assignment content with ChatGPT’s assistance, and
instructors can receive assistance from ChatGPT with administrative and research support
tasks. Ultimately, the following are some of ChatGPT’s major roles and opportunities for
its integration into educational strategies.
4.1. Personalized Learning and Adaptive Education
ChatGPT can enhance learning through boosting productivity and engagement by
providing personalized training and automated grading. In education, personalization
is the process of adjusting curriculum, pedagogy, and learning settings to each student’s
needs and goals. This has historically been a resource-intensive procedure that is frequently
constrained by practical and logistical issues. However, these restrictions have lessened in
the new era of individualized learning ushered in by AI technologies like ChatGPT [26].


## Page 15

Algorithms 2025, 18, 352
15 of 28
Because of its capacity to process and produce language-based content, ChatGPT is a
perfect tool for developing personalized educational resources and experiences. This could
be achieved by utilizing the natural language processing skills of the model to comprehend
the student’s learning needs and tailor the instruction accordingly. Using ChatGPT to create
practice questions specifically tailored to the student is one method to accomplish this [27].
ChatGPT enables personalized learning by adapting to individual student needs, offering
customized feedback, and providing tailored study materials [32]. AI-driven tutoring
can support students at different learning paces, ensuring a more inclusive and effective
learning environment [33].
4.2. Interactive Tutoring
As a personal tutor, ChatGPT can offer students immediate answers, explanations,
and extra materials catered to their individual needs and learning style. This is especially
helpful in large classrooms when teachers may not be able to provide each student the
individualized attention they need [27]. Through interactive coaching, ChatGPT serves
as a personalized instructor to assist users in gradually learning and mastering ideas.
Interactive tutoring has essential elements such as guided learning objectives, question-
based engagement, feedback and clarification, a supportive and adaptive approach, and a
personalized learning pace [28].
4.3. Automated Content Creation and Assessment
Creating content with ChatGPT means using ChatGPT to generate content that not only
informs readers but also engages them. This is accomplished by adding components that
make the content feel more relevant and pleasurable, such as dynamic question-and-answer
forms, relatable examples, interactive storytelling, and personalization [29]. Engaging con-
tent creation is ideal for narratives, blog writing, social media posts, instructional materials,
and more any scenario where maintaining clarity and capturing attention are essential [30].
Educators can use ChatGPT to generate lesson plans, quizzes, and assessments, reducing
workload and allowing them to focus on student engagement [34]. Automated grading
and feedback mechanisms improve efficiency and provide instant evaluation [35].
4.4. Teacher and Student Support
There are several educational advantages to generative artificial intelligence (GAI),
especially when it comes to large language models like ChatGPT, which improve accessibil-
ity and learning. Lesson planning and resources, the ability to explain complex concepts,
assessment and feedback creation, and engagement strategies are just a few of the many
benefits ChatGPT offers teachers. While ChatGPT offers students homework and study sup-
port, concept reinforcement, skill development, encouragement, and confidence building,
the flexibility, speed, and encouraging attitude to instruction with ChatGPT are beneficial
to both educators and learners. ChatGPT’s teacher and student assistance entails providing
tools, resources, and advice specific to teachers and students in order to facilitate instruction
and improve the educational process [28].
4.5. Enhancing Collaborative Learning
By encouraging deeper understanding and enhancing students’ communication
skills, [25] examines the substantial prospects by reorienting students’ attention from
memorization to conceptual comprehension. Collaborative learning is the process of using
ChatGPT’s AI as a facilitator or participant in tasks that promote user cooperation and
shared learning. By organizing, guiding, and facilitating collaborative efforts, ChatGPT can
help make group learning activities more effective and well structured, leading to enhanced
engagement, direction, clarity, and skill development as a result [28]. ChatGPT fosters


## Page 16

Algorithms 2025, 18, 352
16 of 28
interactive learning through AI-powered discussions, simulations, and problem-solving
exercises [36]. Students can use AI-driven platforms to explore concepts in a more engaging
and participatory manner, promoting active learning [37].
4.6. Writing Codes and Assignments
According to the study in [30], ChatGPT can produce coherent answers to assign-
ments and knowledge-based coding tasks. Writing codes and assignments in ChatGPT
means using the AI to assist with coding exercises, programming tasks, and academic
assignments spanning a range of topics. ChatGPT may assist professionals, instructors,
and students in organizing and completing writing assignments in addition to assisting
them in creating, debugging, and understanding code. For coding, creating code, fixing
and debugging errors, optimizing code, elucidating concepts, testing, and documentation
can be achieved [31].
4.7. Bridging Educational Gaps and Accessibility
AI-powered learning tools like ChatGPT can address educational disparities by provid-
ing access to learning resources for underserved communities [38]. ChatGPT can also sup-
port learners with disabilities through speech-to-text, language translation, and accessibility-
friendly interfaces [39].
4.8. Support for Educators and Professional Development
Teachers can use ChatGPT for professional development, accessing AI-driven insights
on curriculum design, student performance analytics, and innovative teaching strate-
gies [40]. The ability to automate administrative tasks also allows educators to focus on
personalized instruction and mentorship [41].
4.9. AI-Powered Learning and Student Engagement
AI-powered educational tools, including ChatGPT, are shown to enhance student
engagement by offering personalized learning experiences. According to [42], adaptive
learning systems powered by AI can cater to individual learning needs by providing
customized feedback and generating dynamic learning materials. Similarly, according
to [43] highlights that ChatGPT fosters interactive learning by facilitating discussions
and enabling real-time question answering. By leveraging these opportunities, ChatGPT
can transform education by fostering innovation, improving learning accessibility, and
enhancing engagement while ensuring ethical and responsible AI integration.
Generally, ChatGPT offers transformative potential in education by enabling person-
alized learning, automated content creation, and interactive tutoring, while supporting
teachers with lesson planning and administrative tasks. It enhances accessibility for under-
served communities and learners with disabilities through features like speech-to-text and
multilingual support. However, challenges such as academic integrity risks, algorithmic
bias, data privacy concerns, and over-reliance on AI must be addressed through ethical
governance, teacher training, and structured integration. Balancing innovation with respon-
sible use is key to harnessing ChatGPT’s benefits without compromising critical thinking
or equity in education.
5. Challenges of Using ChatGPT in Education
5.1. Integration of ChatGPT and Academic Integrity
While AI offers numerous advantages, questions about academic integrity remain. The
study in [44] explains how ChatGPT is used for plagiarism and unauthorized aid in tasks,
posing ethical implications for educators. The work in [45] emphasizes the importance


## Page 17

Algorithms 2025, 18, 352
17 of 28
of combining AI detection methods with ethical principles to address these concerns.
Furthermore, the study in [46] recommends embedding AI literacy training into curricula
to teach students about safe ChatGPT usage.
5.2. ChatGPT and Teacher Workload
ChatGPT is promoted as a tool to reduce teacher workload by automating admin-
istrative tasks such as grading and lesson planning. However, the study in [47] argues
that AI adoption may paradoxically increase teacher responsibilities, as educators must
verify AI-generated content and guide students in its ethical use. The study in [22] calls for
structured AI training programs to help teachers effectively integrate AI tools in classrooms.
5.3. Bias and Ethical Considerations in ChatGPT Models
A critical challenge in AI adoption is the inherent bias in AI-generated content. The
authors of [44] highlight that AI models including ChatGPT are trained on vast datasets
that may contain cultural, gender, and ideological biases. The authors of [45] stress the im-
portance of refining AI models to ensure fairness and accuracy. Additionally, the work [20]
discusses data privacy concerns, emphasizing the need for stringent AI governance policies
to protect student information.
5.4. Lack of Self-Reflection
The AI tool ChatGPT has sparked debate over its potential impact on education. The
disadvantages include a lack of in-depth information, difficulty evaluating the quality of
responses, the risk of prejudice and discrimination, and a lack of higher-order cognitive abil-
ity. Challenges to education include a lack of context awareness, challenges to plagiarism,
the maintenance of educational inequity, and loss of higher-order cognitive capacities [21].
Writing a self-reflection in ChatGPT implies using the AI to help you articulate your ideas,
perceptions, and individual learning experiences, yet choosing not to write a self-reflection
means addressing the project without ChatGPT directly producing the text.
5.5. Lack of Non-Text-Based Responses
ChatGPT’s capacity to handle advanced, non-textual queries limits its effectiveness in
science, technology, engineering, and mathematics (STEM) fields that need complicated
data handling. ChatGPT can tackle intellectually challenging activities, implying that
instructors should reconsider assessment design to include problem-solving tasks that
AI cannot readily perform. However, it has difficulty with more sophisticated activities
that require analysis, interpretation, or non-textual answers, such as drawing structures or
producing graphs [23].
5.6. Does Not Make Predictions About Future Events
ChatGPT is reluctant to make precise predictions or assumptions about the future,
especially when it comes to ambiguous events or outcomes. Rather than making a firm
prediction, it can talk about trends, possibilities, or scenarios based on past patterns or
current knowledge [48].
5.7. Academic Dishonesty
Any behavior that provides an unfair academic advantage or falsifies one’s own work,
knowledge, or abilities in a learning environment is considered academic dishonesty. This
includes behaviors that lead to plagiarism, cheating, and lying about one’s work or accom-
plishments. Because of inaccuracies and a tendency to rely only on artificial intelligence,
ChatGPT in education poses risks to academic integrity and critical thinking [49]. Finally,
the ethical framework that is used is based on striking a balance between the usage of


## Page 18

Algorithms 2025, 18, 352
18 of 28
new technology and societal welfare. However, questions of dependency, ethical use, and
even abuse arise, emphasizing the importance of carefully considering its consequences on
academic dishonesty [50].
Therefore, the integration of ChatGPT in education presents significant challenges
to academic integrity, as it facilitates plagiarism and unauthorized aid, necessitating ro-
bust detection tools and AI literacy programs [44–46]. While it promises to reduce teacher
workload through automation, it paradoxically increases responsibilities by requiring
educators to verify AI-generated content and guide ethical usage [22,47]. Ethical con-
cerns are further compounded by bias in AI outputs and data privacy risks, demanding
stringent governance policies to ensure fairness and security [20,44,45]. Additionally, Chat-
GPT’s limitations—such as its inability to produce self-reflective or non-textual responses
(e.g., STEM visualizations) and its avoidance of future predictions—restrict its applicability
in higher-order cognitive tasks and complex disciplines [21,23,48]. These shortcomings,
combined with risks of academic dishonesty and over-reliance, underscore the need for
balance policies that leverage ChatGPT’s benefits while safeguarding educational integrity
and fostering critical thinking [49,50]. A holistic approach, combining teacher training,
ethical guidelines, and adaptive assessments, is essential to mitigate these challenges and
ensure responsible AI integration in academia.
6. Result and Analysis
6.1. Application of ChatGPT in Education
In response to research question 1, the findings indicate that ChatGPT has been
widely used for personalized learning, interactive tutoring, and content creation. Future
research should explore longitudinal studies to assess the sustained impact of AI on student
performance and engagement. Table 4 provides a summary of key studies, highlighting
their objectives, findings, strengths, and limitations to offer a holistic understanding of
ChatGPT’s role in education.
Table 4. Summary of related works on the applications of ChatGPT in education.
Ref.
Year
Model
Dataset
Approach
Performance
Metrics
Objectives
Main
Findings
Strengths
Limitations
[21]
2023
AI
Ethics
Mixed
academic
data
Policy
analysis
Regulatory
compliance
Examine
governance
challenges
Identified
gaps in AI
policy en-
forcement
Strong
theoretical
framework
No
empirical
testing
[46]
2024
AI Gov-
ernance
AI-driven
education
Ethical AI
implemen-
tation
Fairness,
transparency
Propose
governance
strategies
Need for
interdisci-
plinary
collabora-
tion
Clear recom-
mendations
Lacks
implemen-
tation
details
[49]
2023
ChatGPT
Educational
datasets
AI-driven
tutoring
Student
engagement,
accuracy
Assess
ChatGPT’s
role in
tutoring
Found
increased
engagement
but mixed
accuracy
Strong
empirical
design
Lacks
real-world
case studies
[51]
2023
ChatGPT
University
case
studies
Personalized
learning
model
Learning
outcomes
Evaluate
AI’s impact
on adaptive
learning
Showed
promise in
individual
learning
support
Effective in
low-resource
settings
Bias in
dataset
selection


## Page 19

Algorithms 2025, 18, 352
19 of 28
Similar to prior studies [7,52,53], this review confirms that AI can provide individual-
ized support for students. However, this study also reveals gaps in empirical validation;
many studies focus on potential applications rather than real-world case studies demon-
strating ChatGPT’s effectiveness. Future research should explore longitudinal studies to
assess the sustained impact of AI on student performance and engagement.
6.2. Governance and Policy Challenges
In response to the second research question, the study reveals that governance frame-
works for AI in education are still evolving. Ethical concerns such as academic dishonesty,
AI bias, and data privacy require immediate policy interventions. Unlike earlier studies
that primarily focus on technical challenges [45], this research highlights the socio-political
dimensions of AI adoption, including its impact on teacher workload and institutional
governance structures. The literature underscores the necessity for standardized regula-
tions to ensure AI adoption aligns with educational integrity principles. The adoption
of ChatGPT and other AI tools in education has introduced significant governance and
policy challenges that require immediate attention. This section discusses key concerns,
including ethical considerations, academic integrity, data privacy, and the necessity for
regulatory frameworks.
6.2.1. Ethical Considerations
AI-generated content raises concerns about plagiarism, originality, and student over-
reliance on automated tools. Studies indicate that ChatGPT’s ability to generate well-
structured responses may encourage students to bypass critical thinking and independent
learning [51]. However, institutions must establish strict policies to regulate AI usage,
ensuring that it complements rather than replaces traditional learning approaches [46].
6.2.2. Data Privacy and Security
ChatGPT operates on vast datasets, often processing user-generated content that may
contain sensitive information. This raises concerns about data privacy, user anonymity,
and compliance with education regulations [38]. Without clear policies, institutions risk
exposing student data to unauthorized access and misuse. Future governance efforts must
focus on transparent AI usage policies and secure data management frameworks [20].
6.2.3. AI Bias and Fairness
Bias in AI-generated content remains a critical issue. ChatGPT’s responses are in-
fluenced by training data, which may contain inherent biases related to gender, culture,
or ideology [46]. If left unchecked, biased AI outputs could reinforce stereotypes and
limit diverse perspectives in education. Policymakers must develop evaluation metrics to
regularly audit AI models and mitigate biases [54].
6.2.4. Institutional Governance and Teacher Workload
The integration of AI in education demands institutional governance strategies to
manage teacher workload effectively. While AI can automate administrative tasks, educa-
tors must verify AI-generated content, assess student engagement, and guide ethical AI
usage [40]. Governance frameworks should include teacher training programs to enhance
AI literacy and ensure its responsible implementation in classrooms [47].
6.2.5. Need for Standardized Regulations
The absence of standardized AI policies creates disparities in AI adoption across
institutions. Some universities have embraced ChatGPT as a learning aid, while others
have banned its use due to concerns about academic integrity [33]. Governments and


## Page 20

Algorithms 2025, 18, 352
20 of 28
educational organizations must develop clear AI governance frameworks and regulations
that balance innovation with ethical responsibility [55]. At the end, Table 5 presents a
comprehensive summary of related studies that examine governance and policy challenges
associated with the use of ChatGPT in education. It outlines key issues such as ethical
considerations, regulatory frameworks, institutional policies, and the implications of AI-
driven learning tools. This summary provides valuable insights into the challenges and
potential strategies for effectively integrating ChatGPT within educational institutions.
Moreover, Table 6 illustrates the key governance and policy challenges associated with
the use of AI in education, along with their implications. Addressing these governance
challenges is essential for ensuring the ethical, responsible, and effective integration of
AI technologies like ChatGPT in educational settings. Future research should focus on
developing comprehensive AI policies that uphold academic integrity, mitigate potential
risks, and maximize the benefits of AI in enhancing teaching and learning experiences.
Table 5. Key studies on governance and policy challenges.
Ref.
Key Issue
Findings
Implications
[33]
Lack of Standardization
Institutions have varying policies on
ChatGPT use
A unified AI governance framework
is required to ensure consistency
[38]
Data Privacy
AI systems process sensitive student
data, raising security concerns
Stronger data protection policies and
regulatory compliance are needed
[40]
Teacher Workload
Educators face increased workload in
verifying AI-assisted assignments
Professional development programs
for AI integration should be introduced
[44]
Academic Integrity
AI-generated content may lead to
plagiarism and reduced critical thinking
Institutions must implement AI
literacy programs and detection tools
[46]
Bias in AI Models
AI-generated responses may reflect
biases in training data
Regular auditing and refining of AI
datasets required to reduce bias
Table 6. Summary related works for future research directions.
Ref.
Year
Model
Dataset
Approach
Performance
Metrics
Objectives
Main
Findings
Strengths
Limitations
[43]
2023
AI in Edu-
cation
Large-
scale
academic
data
Compara-
tive study
Institutional
AI policies
Assess AI’s
effectiveness
in diverse
learning
settings
Identified
disparities in
AI adoption
Highlights
accessibility
concerns
Limited to
higher
education
settings
[44]
2023
AI-driven
tutoring
Educational
datasets
Systematic
review
Student
engagement,
accuracy
Enhance
multimodal
learning
beyond
text-based
interactions
Found
potential for
speech
recognition
and
interactive
simulations
Highlights
diverse AI
applica-
tions
Requires
further
empirical
validation
[45]
2023
AI Ethics
Various
education
policies
Theoretical
frame-
work
Ethical
compliance,
bias
reduction
Standardize
AI governance
policies
Identified
gaps in
ethical AI
implementa-
tion
Comprehen-
sive
literature
synthesis
Lacks
empirical
data


## Page 21

Algorithms 2025, 18, 352
21 of 28
Table 6. Cont.
Ref.
Year
Model
Dataset
Approach
Performance
Metrics
Objectives
Main
Findings
Strengths
Limitations
[54]
2023
AI
Cognitive
Effects
Mixed
academic
data
Longitudinal
study
Critical
thinking
development
Examine
long-term
effects of AI
on learning
Found
potential for
skill en-
hancement
but risk of
dependency
Strong
method-
ological
framework
Calls for
extensive
future
research
[56]
2024
AI Gover-
nance
AI-driven
education
Policy
analysis
Fairness,
transparency
Develop
ethical AI
deployment
frameworks
Identified
need for
regulatory
compliance
Clear
governance
recommen-
dations
Lacks
real-world
testing
6.3. Future Research Directions for ChatGPT in Education
In response to research question 3, the study underscores the necessity for robust
regulatory frameworks and structured AI training programs for educators. Prior research
has called for interdisciplinary collaboration between technologists, educators, and poli-
cymakers [56], and this study reinforces that recommendation by emphasizing ethical AI
deployment strategies. Additionally, it identifies the need for empirical research on AI’s
long-term effects on teacher autonomy and student learning outcomes. By integrating the
research questions with related works and findings, this study provides a comprehensive
analysis of ChatGPT’s role in education, offering a nuanced perspective that balances both
opportunities and limitations. Hence, Table 6 shows a summary of related works for future
directions on ChatGPT in education.
6.3.1. Enhancing AI Capabilities for Education
Current AI applications in education are mostly focused on text-based interactions.
However, future studies should look into AI’s capabilities in non-textual activities includ-
ing speech recognition, visual learning aids, and interactive simulations [34]. Creating
multimodal AI models will allow for more inclusive and engaging learning experiences for
students with diverse learning styles [33].
6.3.2. Ethical AI Deployment and Governance Frameworks
As AI’s use in education grows, ethical concerns about data privacy and algorith-
mic prejudice are addressed. Future research should provide comprehensive governance
systems that oversee AI use while assuring adherence to educational norms [57]. Further-
more, interdisciplinary collaboration among educators, technologists, and policymakers is
required to create responsible AI policies [32].
6.3.3. AI’s Long-Term Impact on Educators and Students
The majority of the research focuses on the immediate benefits of ChatGPT in teaching.
However, future research needs look into the long-term impacts on teacher autonomy,
student learning outcomes, and cognitive development [58]. Empirical studies are needed
to assess if AI-powered education improves or degrades critical thinking and problem-
solving abilities over time [36].
6.3.4. AI in Diverse Educational Contexts
While numerous studies look at the function of artificial intelligence in higher educa-
tion, there is little research on its impact in primary and secondary education, vocational
training, and special education. Future research should look into the effectiveness of AI in


## Page 22

Algorithms 2025, 18, 352
22 of 28
a variety of educational settings to ensure its accessibility and inclusivity [38]. Furthermore,
examining AI’s function in bridging the digital divide is critical for encouraging equal
access to AI-driven learning resources.
6.3.5. Standardizing AI Integration in Curricula
To optimize the benefits of AI in education, standardization of AI-driven curriculum
development, teacher training, and student assessment is required. Future studies should
focus on developing AI integration guidelines that are consistent with existing educational
frameworks [33]. Teacher professional development programs should be strengthened to
provide educators with AI literacy and practical implementation skills [14].
The future of AI in education demands multimodal advancements to move beyond
text-based interactions, incorporating speech recognition and visual aids for more inclu-
sive learning [33,34]. However, this expansion must be accompanied by robust ethical
frameworks to address data privacy and algorithmic bias, requiring collaboration across
education, technology, and policy sectors [32,55]. While current research highlights imme-
diate benefits, longitudinal studies are critically needed to assess AI’s long-term effects
on teacher autonomy, student cognition, and skill development [36,59]. Additionally, the
focus must broaden beyond higher education to include K–12, vocational, and special edu-
cation contexts, ensuring equitable access and addressing the digital divide [38,58]. Finally,
standardized curricular integration and teacher training programs are essential to align AI
tools with pedagogical goals while empowering educators to use them effectively [14,33].
Together, these priorities underscore the need for a balanced, research-driven approach to
harness AI’s potential without compromising educational integrity or inclusivity.
7. Key Findings and Implications
The analysis reveals that ChatGPT can enhance personalized learning, provide scalable
tutoring, and automate administrative tasks for educators; however, it also raises concerns
about academic integrity, data privacy, AI biases, and the need for clear governance struc-
tures. The major findings of this study are categorized as follows:
7.1. Teacher Workload and Pedagogical Challenges
While AI can automate routine tasks [57], it may also increase teacher responsibilities
related to verifying AI-generated content and guiding students on proper AI use.
7.2. Enhancing Student Engagement and Learning Outcomes
According to studies [42,43], AI-driven tailored learning improves engagement and
academic performance, particularly for students who require additional support. AI-
powered technologies, such as ChatGPT, can greatly increase student engagement by
delivering quick feedback, creating personalized study materials, and facilitating engaging
discussions. According to studies [28], students who use AI-assisted tutoring systems
enhance their comprehension and retention. However, the extent to which AI has a good
impact is determined by its suitable deployment in connection with pedagogical goals.
7.3. Policy Interventions
According to research [44,45], ChatGPT raises the risk of plagiarism and over-reliance
on AI-generated content, necessitating sophisticated detection and mitigation measures.
The widespread availability of ChatGPT has raised worries about academic dishonesty, as
students may utilize AI to finish assignments without fully grasping the content [58]. To
prevent these threats, institutions must develop stringent academic policies, AI detection
systems, and awareness initiatives. According to research [60], incorporating AI ethics
courses into curricula can help students learn how to use AI responsibly.


## Page 23

Algorithms 2025, 18, 352
23 of 28
7.4. Role of Educators in AI Integration
While AI can automate administrative work, educators play an important role in
guiding students on how to use AI ethically. According to studies [14], professional devel-
opment programs for teachers to train them on AI integration are essential. Policymakers
should provide educators with AI literacy training and curriculum recommendations.
7.5. Addressing AI Bias and Ensuring Data Privacy
ChatGPT’s outputs are influenced by biases in its training data [29], raising questions
about disinformation and fairness in education. ChatGPT’s replies may reflect biases in
its training data [34], providing issues in assuring fair and accurate information delivery.
AI applications also raise issues regarding student data privacy and personal information
security. Future research should focus on improving AI models to reduce biases and
creating strong data governance policies [61].
7.6. Summary of Research Questions
As illustrated in Table 7, the following research questions were addressed: (1) How
has ChatGPT been applied in education? The findings show that ChatGPT is utilized
for personalized learning, tutoring, and content creation. However, its application lacks
real-world validation [31,51]. (2) What are the major governance and policy challenges?
The findings show that major challenges include ethical concerns, academic dishonesty, AI
bias, data privacy issues, and increased teacher workload [45]. (3) What future research
directions are needed? The findings show there is a need for regulatory frameworks, AI
literacy programs, and empirical validation of AI in education [39].
Table 7. Summary of research questions and findings.
Ref.
Research Question
Findings from This Study
[31]
How has ChatGPT been applied in education?
Used for personalized learning, tutoring, and content
creation; lacks real-world validation
[39]
What future research directions are needed?
Need for regulatory frameworks, AI literacy programs,
empirical validation of AI in education
[45]
What are the major governance and policy
challenges?
Ethical concerns, academic dishonesty, AI bias, data
privacy, and teacher workload issues
Based on the findings across 40 peer-reviewed studies, it is evident that ChatGPT
integration in education yields both pedagogical opportunities and ethical concerns. For
example, studies such as [1,7] illustrate enhanced student engagement and personalized
learning pathways due to ChatGPT’s adaptability. However, others like [5,6] emphasize the
growing risks of academic dishonesty and over-reliance on AI. Synthesizing these perspec-
tives reveals a dual reality: while AI-driven tools like ChatGPT can transform educational
delivery, their integration must be accompanied by clear ethical guidelines and adaptive
teaching strategies. Unlike earlier studies that focused narrowly on either opportunity or
risk, this review bridges both to propose a balanced framework for future implementation.
8. Future Research Directions
Several studies emphasize the need for ongoing research to refine AI’s role in education.
Key areas include the following.
8.1. Personalized Adaptive Learning
AI-powered systems should grow to offer real-time, adaptive learning paths based on
individual students’ strengths and weaknesses. Future studies should look into how deep


## Page 24

Algorithms 2025, 18, 352
24 of 28
learning models can improve personalization while still promoting student autonomy and
critical thinking [59].
8.2. AI Ethics and Bias Mitigation
Addressing bias, misinformation, and ethical issues in AI-generated material is crucial.
Future research should concentrate on establishing transparent AI models that reduce
biases and adhere to educational equity and inclusivity [59,61].
8.3. Regulatory Frameworks and Governance
Policymakers have to establish comprehensive governance mechanisms to oversee AI
in education while balancing innovation and ethical safeguards. Future research should
look at how global AI policies affect education systems and student data privacy [61,62].
This paper expands on previous research by thoroughly assessing ChatGPT’s role in
education, identifying governance problems, and recommending future research topics for
responsible AI adoption.
8.4. Human–AI Collaboration in Teaching
Instead of replacing instructors, AI could serve as an intelligent helper to improve
teaching efficacy. Research should look at teacher AI interaction models and assess their
impact on classroom engagement and curriculum design [14].
8.5. AI-Driven Tutoring Systems
AI-powered intelligent tutoring systems are created to give individualized learning
experiences tailored to each student’s needs and learning pace [40].
8.6. Interdisciplinary Collaboration for Responsible AI Governance
Effective AI integration in education necessitates collaboration among educators,
technologists, and lawmakers to develop ethical principles and governance structures that
promote responsible use [44].
8.7. Evaluating AI’s Effectiveness Across Diverse Educational Settings
Ongoing research is required to analyze the impact of AI tools such as ChatGPT in
diverse educational contexts, ensuring that they improve learning outcomes while avoiding
biases or inaccuracies [41].
8.8. AI for Under-Resourced Learning Environments
Future research should focus on making AI accessible and scalable in low-resource
settings, ensuring that developing regions benefit from AI-driven education while not
worsening digital divides [61]. Hence, the future of AI in education hinges on developing
adaptive learning systems that personalize instruction while preserving student autonomy
and critical thinking [59], coupled with rigorous bias mitigation to ensure equitable, trans-
parent AI outputs [62]. Effective implementation requires multi-stakeholder governance
frameworks that balance innovation with ethical safeguards, particularly for data privacy
and global policy alignment. Crucially, AI should augment rather than replace teachers,
with research needed on optimal human–AI collaboration models to enhance pedagogy [14]
and intelligent tutoring systems [40]. This demands interdisciplinary cooperation among
educators, technologists, and policymakers to establish ethical guidelines [44], alongside
expanded studies on AI’s efficacy in diverse contexts from K-12 to under-resourced settings
to bridge digital divides without exacerbating inequalities [41,62]. Together, these priorities
underscore a vision for AI as a scalable, equitable tool that complements human expertise
while addressing systemic educational challenges.


## Page 25

Algorithms 2025, 18, 352
25 of 28
Finally, to strengthen the analytical rigor of this study, we have revised the manuscript
to provide a substantive synthesis of the literature. The revised sections now clearly distin-
guish between the 40 systematically reviewed studies and supplementary contextual refer-
ences (>40), ensuring methodological transparency. Sections on opportunities, challenges,
and future directions have been restructured to align directly with the research questions,
offering comparative insights and thematic integration from the reviewed studies, while
supplementary references contextualize broader implications. This enhanced organization,
including the addition of the PRISMA 2020 framework citation, facilitates a critical analysis
of trends, gaps, and ChatGPT’s educational role, moving beyond descriptive reporting
toward actionable conclusions.
9. Conclusions
ChatGPT has the potential to improve education by making it more personalized,
accessible, and interactive for teachers and students alike. However, issues of privacy,
data security, and ethical use must be addressed. This study emphasizes ChatGPT’s
function in assisting with theory-based queries, developing ideas for application-based
questions, and incorporating technology into teaching. Teachers can also use it during
workshops to review and evaluate AI-generated responses. Despite its benefits, ChatGPT
has drawbacks, including the danger of academic dishonesty and reliance, which can
impair critical thinking. It can be difficult for educators to distinguish between learners who
actively engage with the curriculum and those who rely on automation. Notably, ChatGPT
paraphrases comments in ways that bypass similarity detection technologies, prompting
upgrades to plagiarism detection tools. Future research should focus on enhancing AI’s
ability to perform non-textual jobs, creating more powerful AI content identification tools,
and resolving ethical concerns about academic integrity and data protection. Additionally,
policies and teacher training programs are required to enable responsible AI incorporation.
Collaboration between educators, legislators, and technology providers is essential for
defining guidelines, improving professional development, and closing the digital gap.
Finally, this review serves as a foundational resource for stakeholders navigating AI’s role in
education, advocating for proactive governance and further empirical research. Therefore,
we provide the following key recommendations for stakeholders: (1) Educators should
integrate AI literacy into curricula and use ChatGPT as a supplement, not a substitute.
(2) Policymakers should consider developing standardized regulations to ensure equitable
and responsible AI use. (3) Researchers are also expected to prioritize empirical studies
on AI’s long-term pedagogical impact and bias mitigation. By addressing these gaps,
stakeholders can harness ChatGPT’s potential while safeguarding educational integrity
and inclusivity.
Author Contributions: The work presented here was carried out in collaboration among all authors.
Conceptualization, Y.Y.M. and W.A.; formal analysis, Y.Y.M. and Y.B.; methodology, A.M. and Y.Y.M.;
supervision, M.A.; visualization, Y.Y.M. and W.A.; writing—original draft, M.A.; writing—review
and editing, Y.B. and A.M., Fund Acquisition, W.A. All authors have read and agreed to the published
version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: The dataset can be available upon request.
Conflicts of Interest: The authors declare no conflict of interest.


## Page 26

Algorithms 2025, 18, 352
26 of 28
References
1.
Farrokhnia, M.; Noroozi, O.; Wals, A.E.J. A SWOT analysis of ChatGPT: Implications for educational practice and research. Innov.
Educ. Teach. Int. 2024, 61, 460–474. [CrossRef]
2.
Ouyang, F.; Wu, M.; Zheng, L.; Zhang, L.; Jiao, P. Integration of artificial intelligence performance prediction and learning
analytics to improve student learning in online engineering course. Int. J. Educ. Technol. High. Educ. 2023, 20, 4. [CrossRef]
[PubMed]
3.
Yu, X. Assessment of systemic AAV-microdystrophin gene therapy in the GRMD dog model. Mol. Ther. 2024, 31, 123–135.
4.
Acosta-Enriquez, B.G.; Ballesteros, M.A.A.; Vargas, C.G.A.P.; Ulloa, M.N.O.; Ulloa, C.R.G.; Romero, J.M.P.; Jaramillo, N.D.G.;
Orellana, H.U.C.; Anzoátegui, D.X.A.; Roca, C.L. Knowledge, attitudes, and perceived ethics regarding the use of ChatGPT
among Generation Z university students. Int. J. Educ. Integr. 2024, 20, 10. [CrossRef]
5.
Grassini, S. Shaping the future of education: Exploring the potential and consequences of AI and ChatGPT in educational settings.
Educ. Sci. 2023, 13, 692. [CrossRef]
6.
Anders, B.A. Is using ChatGPT cheating, plagiarism, both, neither, or forward thinking? Patterns 2023, 4, 100694. [CrossRef]
7.
Crompton, H.; Burke, D. The educational affordances and challenges of ChatGPT: State of the field. TechTrends 2024, 68, 380–392.
[CrossRef]
8.
Guo, Y.; Lee, D. Leveraging ChatGPT for enhancing critical thinking skills. J. Chem. Educ. 2023, 100, 4876–4883. [CrossRef]
9.
Gill, S.S.; Xu, M.; Patros, P.; Wu, H.; Kaur, R.; Kaur, K.; Fuller, S.; Singh, M.; Arora, P.; Parlikad, A.K.; et al. Transformative effects
of ChatGPT on modern education: Emerging era of AI chatbots, Internet of Things and cyber-physical systems. Internet Things
Cyber-Phys. Syst. 2024, 4, 19–23. [CrossRef]
10.
Mai, D.T.T.; Da, C.V.; Hanh, N.V. The use of ChatGPT in teaching and learning: A systematic review through SWOT analysis
approach. Front. Educ. 2024, 9, 1328769. [CrossRef]
11.
Dempere, J.; Modugu, K.; Hesham, A.; Ramasamy, L.K. The impact of ChatGPT on higher education. Front. Educ. 2023, 8, 1206936.
[CrossRef]
12.
Ray, P. ChatGPT: A comprehensive review on background, applications, key challenges, bias, ethics, limitations and future scope.
Internet Things Cyber-Phys. Syst. 2023, 3, 121–154. [CrossRef]
13.
Emenike, M.E.; Emenike, B.U. Considerations for Artificial Intelligence Text-Generation Software Programs for Chemists and
Chemistry Educators. J. Chem. Educ. 2023, 100, 1413–1418. [CrossRef]
14.
Ahmad, N.; Murugesan, S.; Kshetri, N. Generative artificial intelligence and the education sector. Computer 2023, 56, 72–76.
[CrossRef]
15.
Chocarro, R.; Cortiñas, M.; Marcos-Matás, G. Teachers’ attitudes towards chatbots in education: A technology acceptance model
approach considering the effect of social language, bot proactiveness, and users’ characteristics. Educ. Stud. 2023, 49, 295–313.
[CrossRef]
16.
Gardner, D.E.; Giordano, A.N. The Challenges and Value of Undergraduate Oral Exams in the Physical Chemistry Classroom:
A Useful Tool in the Assessment Toolbox. J. Chem. Educ. 2023, 100, 1705–1709. [CrossRef]
17.
Al-kfairy, M. Factors impacting the adoption and acceptance of ChatGPT in educational settings: A narrative review of empirical
studies. Appl. Syst. Innov. 2024, 7, 110. [CrossRef]
18.
Fergus, S.; Botha, M.; Ostovar, M. Evaluating academic answers generated using ChatGPT. J. Chem. Educ. 2023, 100, 1672–1675.
[CrossRef]
19.
Mengist, W.; Soromessa, T.; Legese, G. Method for conducting systematic literature review and meta-analysis for environmental
science research. MethodsX 2020, 7, 100777. [CrossRef]
20.
Gaševi´c, D.; Siemens, G.; Sadiq, S. Empowering learners for the age of artificial intelligence. Comput. Educ. Artif. Intell. 2023,
4, 100130. [CrossRef]
21.
Benuyenah, V. Commentary: ChatGPT use in higher education assessment: Prospects and epistemic threats. J. Res. Innov. Teach.
Learn. 2023, 16, 134–135. [CrossRef]
22.
Abujaber, A.A.; Abd-Alrazaq, A.; Al-Qudimat, A.R.; Nashwan, A.J. A strengths, weaknesses, opportunities, and threats (SWOT)
analysis of ChatGPT integration in nursing education: A narrative review. Cureus 2023, 15, e48643. [CrossRef] [PubMed]
23.
Akgun, S.; Greenhow, C. Artificial intelligence in education: Addressing ethical challenges in K-12 settings. AI Ethics 2022, 2,
431–440. [CrossRef] [PubMed]
24.
Black, J. Past, present and tackling the future of artificial intelligence (AI) in education: Maintaining agency and establishing AI
laws. Open J. Soc. Sci. 2023, 11, 442–464. [CrossRef]
25.
Lima, A.R.; Lima, I.N.; Guevara-Soto, F.J. Challenges and opportunities of AI-assisted learning: A systematic literature review on
the impact of ChatGPT usage in higher education. Int. J. Learn. Teach. Educ. Res. 2023, 22, 122–135.
26.
Labadze, L.; Grigolia, M.; Machaidze, L. Role of AI chatbots in education: Systematic literature review. Int. J. Educ. Technol. High.
Educ. 2023, 20, 56. [CrossRef]


## Page 27

Algorithms 2025, 18, 352
27 of 28
27.
Okonkwo, C.W.; Ade-Ibijola, A. Chatbots applications in education: A systematic review. Comput. Educ. Artif. Intell. 2021,
2, 100033. [CrossRef]
28.
Ramandanis, D.; Xinogalos, S. Investigating the support provided by chatbots to educational institutions and their students:
A systematic literature review. Multimodal Technol. Interact. 2023, 7, 103. [CrossRef]
29.
Baidoo-Anu, D.; Ansah, L.O. Education in the era of generative artificial intelligence (AI): Understanding the potential benefits of
ChatGPT in promoting teaching and learning. J. AI 2023, 7, 52–62. [CrossRef]
30.
Mhlanga, D. ChatGPT in Education: Exploring Opportunities for Emerging Economies to Improve Education with ChatGPT.
SSRN. 2023. [CrossRef]
31.
Su, J.; Yang, W. Unlocking the power of ChatGPT: A framework for applying generative AI in education. ECNU Rev. Educ. 2023,
6, 355–366. [CrossRef]
32.
Yang, S.; Evans, C. Opportunities and challenges in using AI chatbots in higher education. In Proceedings of the 2020 ACM
Conference on Innovation and Technology in Computer Science Education, Trondheim, Norway, 15–19 June 2020; ACM:
New York, NY, USA, 2020; pp. 1–6. [CrossRef]
33.
Zamir, S.; Afzal, S.; Sultana, N. ChatGPT and artificial intelligence in higher education institutions: Benefits, challenges and
ethical concerns. Biannu. Uswa J. Res. 2023, 3, 2.
34.
Sobaih, A.E.E.; Elshaer, I.A.; Hasanein, A.M. Examining students’ acceptance and use of ChatGPT in Saudi Arabian higher
education. Eur. J. Investig. Health Psychol. Educ. 2024, 14, 709–721. [CrossRef] [PubMed]
35.
Almogren, A.S.; Al-Rahmi, W.M.; Dahri, N.A. Exploring factors influencing the acceptance of ChatGPT in higher education:
A smart education perspective. Heliyon 2024, 10, e31887. [CrossRef] [PubMed]
36.
Imran, M.; Almusharraf, N. Analyzing the role of ChatGPT as a writing assistant at higher education level: A systematic review
of the literature. Contemp. Educ. Technol. 2023, 15, ep464. [CrossRef]
37.
Singh, M. Maintaining the integrity of the South African university: The impact of ChatGPT on plagiarism and scholarly writing.
S. Afr. J. High. Educ. 2023, 37, 203–220. [CrossRef]
38.
Kuhail, M.A.; Alturki, N.; Alramlawi, S.; Alhejori, K. Interacting with educational chatbots: A systematic review. Educ. Inf.
Technol. 2023, 28, 973–1018. [CrossRef]
39.
Yu, J. AI-driven educational reforms: Challenges and opportunities. Int. J. Educ. Technol. 2024, 47, 140–159.
40.
Guo, Y.; Lee, K. AI accessibility in education: Challenges and solutions. Int. J. Educ. Technol. 2023, 45, 189–207.
41.
Grassini, S. AI in personalized learning: Enhancing student engagement. J. Educ. AI Res. 2023, 21, 150–167.
42.
Guo, Y.; Lee, K. University policies on AI: A comparative analysis. J. High. Educ. Policy 2023, 45, 122–138.
43.
Ray, S. Unmasking bias in AI-generated educational content. AI Educ. Rev. 2023, 15, 110–128.
44.
Zhou, H.; Patel, M.; Gomez, R. AI governance in higher education: Bias, misinformation, and policy gaps. J. AI Ethics Regul. 2023,
19, 55–73.
45.
Abujaber, R.; Khan, F.; Patel, M. Data privacy in AI-powered learning systems: Challenges and solutions. AI Soc. 2023, 39,
199–215.
46.
Farrokhnia, M.; Esmaeili, A.; Rahmani, L. AI-powered teacher support: Balancing automation and human oversight. Technol.
Educ. J. 2024, 33, 89–104.
47.
Crompton, H.; Burke, M. Ethical AI in education: Addressing bias and accountability. Comput. Educ. 2024, 185, 103–120.
48.
Victor, D. Factors and impacts of ChatGPT adoption for academic purposes in higher learning institutions: Students’ perspectives.
SSRN Electron. J. 2024. [CrossRef]
49.
Liao, C.; Wang, M. AI-powered learning platforms: Evaluating student engagement and retention. J. Learn. Sci. 2023, 28, 205–224.
50.
Huang, Z.; Wang, M.; Yang, K. The impact of ChatGPT on the learning efficacy of Chinese college students. Lect. Notes Educ.
Psychol. Public Media 2023, 21, 289–298. [CrossRef]
51.
Huang, T.; Zhang, F.; Chen, L. Fostering interactive learning with AI: The case of ChatGPT. Educ. Technol. Soc. 2023, 26, 120–138.
52.
Smith, K.; Lee, R. Accessibility and AI in education: A review of assistive technologies. J. Learn. Disabil. Technol. 2022, 15, 56–72.
53.
Benuyenah, A. AI in student engagement: The role of chatbots in higher education. Educ. Technol. Res. Dev. 2023, 71, 178–194.
54.
Farrokhnia, M.; Banihashem, S.K.; Noroozi, O.; Wals, A. AI in teaching and learning: Opportunities and challenges. Int. J. Educ.
Technol. 2024, 45, 189–205.
55.
Anders, P. Artificial Intelligence and Academic Integrity: Challenges and Solutions, 1st ed.; Routledge: New York, NY, USA, 2023.
56.
Akgun, O.; Greenhow, C. The role of AI in education: Risks and rewards for critical thinking development. Comput. Educ. 2022,
189, 102–119.
57.
Abujaber, R.; Al-Khasawneh, M.; Shalaby, L. AI in education: Balancing privacy concerns and innovation. IEEE Trans. Learn.
Technol. 2023, 17, 214–228.
58.
Aoun, R.; Aldowah, G.I. AI-driven personalized learning: An adaptive framework for student engagement. Comput. Educ. Artif.
Intell. 2022, 3, 100067. [CrossRef]


## Page 28

Algorithms 2025, 18, 352
28 of 28
59.
Wang, J.; Hussain, Y.; Zhang, X.; Mao, C.; Wu, Z. AI-Based Automated Grading Systems: Opportunities, Challenges, and Future
Directions. Bus. Soc. Sci. Proc. 2025, 1, 29–39. [CrossRef]
60.
UNESCO. Use of AI in Education: Deciding the Future We Want. UNESCO Report on AI and Education. 2023. Available online:
https://www.unesco.org/en/articles/use-ai-education-deciding-future-we-want (accessed on 10 January 2025).
61.
Ferrara, E. Fairness and Bias in Artificial Intelligence: A Brief Survey of Sources, Impacts, and Mitigation Strategies. Sci 2024, 6, 3.
[CrossRef]
62.
Yang, S.J.; Ogata, H.; Matsui, T.; Chen, N.-S. Human-centered artificial intelligence in education: Seeing the invisible through the
visible. Comput. Educ. Artif. Intell. 2021, 2, 100008. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.


---

## Notes
- Auto-converted from PDF
- Please review and clean up formatting as needed
- Add manual annotations and summaries above this line
