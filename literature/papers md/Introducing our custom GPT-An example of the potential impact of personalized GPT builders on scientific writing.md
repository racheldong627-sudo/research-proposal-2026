# Literature Review: Introducing our custom GPT-An example of the potential impact of personalized GPT builders on scientific writing

**Source:** `papers pdf/Introducing our custom GPT-An example of the potential impact of personalized GPT builders on scientific writing.pdf`  
**Converted:** 2025-11-05 15:15:40  
**Status:** Auto-converted from PDF using PyMuPDF  

---



## Page 1

Introducing Our Custom GPT: An Example of the Potential Impact of Personalized
GPT Builders on Scientiﬁc Writing
Aymen Kabir1, Suraj Shah2, Alexander Haddad1, Daniel M.S. Raper1
- BACKGROUND: The rapid progression of artificial in-
telligence (AI) and large language models (LLMs), such as
ChatGPT, has contributed to increase its utility and popu-
larity in various fields. Discourse about AI’s potential role
in different aspects of scientific literature such as writing,
data analysis, and literature review, is growing as the
programs continue to improve their capabilities. This study
utilizes a recently released ChatGPT tool that allows users
to create customized GPTs to highlight the potential of
customizable GPTs tailored to prepare and write research
manuscripts.
- METHODS: We developed our 2 GPTs, Neurosurgical
Research Paper Writer and Medi Research Assistant,
through iterative refinement of ChatGPT 4.0’s tool, GPT
Builder. This process included providing specific and
thorough instructions along with repetitive testing and
feedback-driven adjustments to finalize a version of the
model that fit our needs.
- RESULTS: The GPT models that we created were able to
efficiently and consistently produce accurate outputs from
inputted prompts based on their specific configurations. It
effectively analyzed existing literature that it found and
synthesized information in ways that were reliable and
written in ways comparable to manuscripts authored by
scientific professionals.
- CONCLUSIONS: While the ability of modern AI to
generate scientific manuscripts has shown significant
progress, the persistence of fallacies and miscalculations
suggest that the development of GPTs requires extensive
calibration
before
achieving
greater
reliability
and
consistency. Nevertheless, the prospective horizon of AI-
driven research holds promise in streamlining the publi-
cation workflow and increasing accessibility to novel
research.
INTRODUCTION
T
he use of artiﬁcial intelligence (AI), and ChatGPT in
particular, has been gaining traction in various ﬁelds as
large language models (LLMs) continue to improve their
utility. In medical literature, different chatbots have proven to be
useful in aiding with the writing processes as well as data anal-
ysis. The impact of ChatGPT has been noted in various ﬁelds
including, but not limited to, medical education, scientiﬁc writing,
research, and diagnostic decision-making.1,2 AI-based programs
have been found to aid in writing sections of scientiﬁc papers
while correcting grammatical errors and improving overall writing
style and have been noted to be of particular interest to non-
native English speakers in which writing can be the most difﬁ-
cult task of publishing scientiﬁc work.3
However, many examples highlight falsiﬁed products that include
fabricated data and studies, manipulated data, as well as plagia-
rism of existing bodies of work.4,5 These ﬁndings can be difﬁcult
to ascertain for the researchers utilizing these programs without
using ample time to thoroughly review any product of the
chatbot. This, in turn, defeats one of the main purposes of
utilizing AI— allowing writing and data analysis to be done both
effectively and efﬁciently.
The most notable shortcoming of AI in medical writing and
research has been its ability to hallucinate data which can
contribute to fraudulent scientiﬁc papers that, at ﬁrst glance, can
appear to be legitimate to the reader. Additionally, while AI can in
Key words
- Artificial intelligence
- ChatGPT
- GPT builder
- Large language models
- Medical literature
- Scientific writing
Abbreviations and Acronyms
AI: Artificial intelligence
LLM: Large language model
From the 1Department of Neurological Surgery, University of California, San Francisco; and
2University of California, Berkeley, California, USA
To whom correspondence should be addressed: Daniel M. S. Raper, M.B.B.S.
[E-mail: Daniel.raper@ucsf.edu]
Citation: World Neurosurg. (2025) 193:461e468.
https://doi.org/10.1016/j.wneu.2024.10.041
Journal homepage: www.journals.elsevier.com/world-neurosurgery
Available online: www.sciencedirect.com
1878-8750/ª 2025 The Authors. Published by Elsevier Inc. This is an open access article
under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
WORLD NEUROSURGERY 193: 461e468, JANUARY 2025
www.journals.elsevier.com/world-neurosurgery
461
Technical Note


## Page 2

some cases provide unbiased input on different projects, its in-
teractions with the user and the intentions of the user can allow
for the development of biased supporting arguments that use
hallucinated data and literature. With the hallucination of existing
literature also comes the concern of plagiarism. It is important to
note that although these concerns with AI can originate from the
programs themselves, they can often be elicited or worsened by
the inputs of the users. Studies have shown that human re-
viewers have had difﬁculty recognizing the abstracts as the work
of AI alone let alone any potential fabrications that may accom-
pany the ﬁnished products.6 When considering utilizing AI in
medical writing it is imperative to consider these factors as
they go against core principles of scientiﬁc research and
resulting literature.
As LLMs continue to improve in terms of utility, accessibility, and
personalization, it is important to consider the question of what is
“original” and what is “plagiarism” when using AI to assist in
writing literature. Upon the release of ChatGPT 4.0, the most
advanced version of the chatbot to date, OpenAI has begun to
allow users to create their own “GPTs”. These GPTs are
autonomous chatbots that develop certain patterns of responses
and outputs that are catered to the user’s preference. The user
works with the chatbot to delineate particular goals that are
speciﬁc to each GPT and allow for the conﬁguration of the AI in a
way that produces speciﬁc, accurate, and consistent outputs that
match the aims of the user.
In this paper, we intend to highlight the use of customized GPTs
as a more accurate and speciﬁc way of utilizing AI to produce
writing that can be used in research papers. With our GPT,
Neurosurgical Research Paper Writer, we provide an example of
creating an effective tool that overcomes several concerns of AI
programs. Our most recent version of Neurosurgical Research
Paper Writer is able to consistently and reliably search through
existing literature, read and summarize PDFs of relevant ﬁndings,
and build a ﬁnished product that is structured and speciﬁc to the
inputs used to create the GPT. Future personalized LLMs built
from speciﬁc and tailored inputs have the potential to improve
the use of AI in medical literature while avoiding key concerns
such as hallucinations and plagiarism.
Building Neurosurgical Research Paper Writer
To achieve the objective of creating an AI program that can reli-
ably write medical literature we ﬁrst gained access to ChatGPT
4.0’s beta which allows for the use of the GPT builder function.
The GPT builder includes a “create” section that involves con-
versations with the AI that allows it to autonomously create in-
structions and actions that are highlighted in the “conﬁgure”
section of the tool.
Once prompted by the GPT builder, we initiated conversations by
providing concise and speciﬁc asks that allowed the program to
create initial conﬁgurations that are utilized to produce the writing
desired.
The
conversation
with
the
chatbot
continued
by
providing more speciﬁc details including, but not limited to,
writing style, word counts, and structure. Initial conﬁgurations
such as instructions, conversation starters for the chatbot, ca-
pabilities, and speciﬁc actions were then created by the AI and
shared with us for review. Before tailoring these conﬁgurations
to include all of the speciﬁc requirements, we tested the initial
product in what is called the GPT’s “playground” (Figure 1).
The playground was used to initiate conversations and produce
initial abstracts and manuscripts that allowed us to analyze
existing problems that needed to be addressed in further itera-
tions of the GPT. This process included fact-checking the writing
products, as well as asking the AI directly where information was
found and how it was analyzed. We then returned to the
“create” section and engaged in further conversation to address
what was found to allow the AI to re-conﬁgure its settings to
Figure 1. An overview of the layout of OpenAI’s GPT
builder that allows for the creation and conﬁguration of
personalized settings for user-created GPTs. The left
side shows the conversations that create relevant
conﬁgurations that the GPT uses while the right side
represents the “playground” where the conﬁgurations
can be tested before further edits are made.
462
www.SCIENCEDIRECT.com
WORLD NEUROSURGERY, https://doi.org/10.1016/j.wneu.2024.10.041
TECHNICAL NOTE


## Page 3

more accurately represent the goals we had set for the GPT. The
additional instructions included word limits for sections, speciﬁc
online resources to gather data and literature from, and citation
methods intended to prevent plagiaristic hallucinations.
Although GPTs have become infamous for their hallucinations
and lack of consistency, there are multiple ways to control the
GPT’s outputs to ascertain the legitimacy of its responses and
avoid these concerns, one of which depends on the formatting of
commands. To start, we discovered an inconsistency in its ability
to ﬁnd real articles online, with a majority of those produced
being “hypothetical.” After asking the GPT to create an abstract
analyzing existing literature, it provided a complete product that
was based on almost entirely hallucinated studies. As the initial
abstract provided speciﬁc numbers of clinical trials, patients, and
numerical outcomes, it can be easy to accept the ﬁnished
product as truthful. The falsiﬁed sources were not recognized
until the GPT was asked to provide in-text citations as well as a
references section which produced sources published in future
times (i.e. April 2026). Upon this recognition and before providing
further speciﬁcations, we asked the GPT itself about our suspi-
cions and it produced a response that admitted the hallucination
of data (Figure 2).
Another issue we encountered was the GPT’s inability to access
certain pages, notably ones that contained the complete editions
of research articles, thereby limiting the information the GPT can
extract to only the abstracts of these articles. Given that the GPT
is able to access and read PDF ﬁles, we decided to download
each full article and upload it back into the GPT to ensure that
each source is fully utilized (Figure 3). Additionally, uploading the
sources separately for inspection minimizes errors in reading due
to excessive inputs.
The GPT also encounters a token limit that prevents its produced
message from exceeding a certain length, which would result in
a manuscript that is too brief and may exclude important infor-
mation. In Neurosurgical Research Paper Writer, we provided
speciﬁc instructions directing the GPT to write each section
separately and to ensure it matches a certain word range
(Figure 4).
Through various reiterations of our inputs and resulting outputs
we noted that using a GPT to write a research paper involves a
variety of processes, from online searches and analysis of rele-
vant research articles to writing the predetermined sections of
manuscripts. This at times led to confusion and difﬁculties
maintaining consistency. Since providing instructions to use real
databases still allowed for the Neurosurgical Research Paper
Writer to produce fabricated information, we moved forward by
ﬁnding a way to ensure the use of legitimate sources. One
method we used to specialize tasks and avoid confusion be-
tween the functions was the delocalization of these tasks to
multiple GPTs.
After ﬁnalizing our research paper writer, we developed a GPT
named Medi Research Assistant whose sole function is to ﬁnd
relevant literature to a posed question (Figure 5). By asking the
GPT to provide the URL for each source it found, it was able to
avoid nonexistent sources since there would not be a URL to
attach. Asking for any element of the source, such as the
authors or date of publication, should yield the same result.
Medi Research Assistant was conﬁgured to accompany each
source found with a brief summary of the objectives, methods,
and results. This was intended to optimize the time spent
searching through literature for studies that would be uploaded
into the Neurosurgical Research Paper Writer as PDFs. Using a
separate GPT to ﬁnd relevant and legitimate articles on the web
and summarize them allowed for more consistent and reliable
searches of existing literature. Using Medi Research Assistant to
enhance the process of reviewing existing literature allows for
efﬁcient extraction of important results and data that could be
used to decide which sources should be inputted into the
Neurosurgical Research Paper Writer for incorporation into any
ﬁnal manuscript or abstract.
FINAL RESULTS: USABILITY, ADVANTAGES, AND LIMITATIONS OF
THE MODEL
Many LLM, including ChatGPT, have developed a reputation for
producing misinformation through hallucinations or incorrect
calculations. However, formatting commands properly or giving
speciﬁc instructions for the GPT to follow can result in minimal
errors.
One consistent ﬁnding throughout our tests with Neurosurgical
Research Paper Writer was that overloading the GPT with in-
structions occasionally resulted in the GPT “forgetting” to
consider everything included, however through specialization of
tasks, we were able to achieve more elaborate and accurate
responses. Additionally, keeping fewer, but more speciﬁc, in-
structions seemed to ensure that the GPT did not exclude any
directions and completed each one as desired. Although research
articles aren’t constrained to rigid word counts, Neurosurgical
Research Paper Writer would automatically resort to condensing
sections, thus omitting important information if word counts
were not speciﬁed.
Figure 2. An example of reviewing the GPT’s output and asking the
artiﬁcial intelligence (AI) itself about the validity of its product.
WORLD NEUROSURGERY 193: 461e468, JANUARY 2025
www.journals.elsevier.com/world-neurosurgery
463
TECHNICAL NOTE


## Page 4

So far, we have seen that an LLM capable of browsing the web,
such as GPT-4, can rapidly extract relevant information about any
research topic and provide accurate summaries. Although the
GPT may be limited from accessing certain online sources,
particularly the complete documents accompanying research
abstracts, they are still able to provide the user with the URL to
sources as well as a general summary, thereby saving the time it
would normally take for a human to ﬁlter through appropriate
sources.
As Medi Research Assistant currently stands, its instructions to
search through various libraries remains generic and without
speciﬁcations such as prioritizing speciﬁc forms of literature as
they pertain to the topic it is researching. However, the user can
request Medi Research Assistant to ﬁlter for certain types of
Figure 3. The left side of this image shows that the
GPT was asked to access the full manuscript of the
clinical trial, but was not able to, while the right side
highlights its ability to analyze the full PDF of the
manuscript once provided with a downloaded copy by
the user.
Figure 4. The left side provides an example of the
GPT’s output without the speciﬁcation of writing each
section of the manuscript separately; the right side
highlights the product of a single section once the
speciﬁcation is applied.
464
www.SCIENCEDIRECT.com
WORLD NEUROSURGERY, https://doi.org/10.1016/j.wneu.2024.10.041
TECHNICAL NOTE


## Page 5

sources, such as randomized trials or reviews, depending on their
preferences.
Reviewing the draft after it has been written is imperative.
Regardless of how detailed the initial instructions were, language
models are not exempt from making mistakes, so there may still
be ﬂaws in logic, miscalculations, or even errors in the informa-
tion provided. However, cross-checking the GPT against itself by
providing it the same prompt in a new window may help deter-
mine inconsistencies in the information.
While there is no single metric that can measure the GPTs utility,
the results that it has created thus far show promise in its ability
to follow clearly delineated instructions and methods while
accurately citing real sources in an appropriate manner. After
ﬁnalizing the current settings of GPTs, we instructed Neurosur-
gical Research Paper Writer to create its own manuscript based
on
the
topic
of
this
paper
(Supplementary
Material
1).
Neurosurgical Research Paper Writer was able to properly
implement in-text citations, create a bibliography in AMA
format, and construct a layout similar to our own paper. We were
able to modify the depth of information provided in each section
by adjusting the word count and instructing the GPT to provide
either more or less detail as needed. Though there were some
minor issues, such as the GPT referring to itself in the ﬁrst per-
son in the manuscript’s ﬁrst rendition, it was quickly able to
correct itself after we instructed it to do so.
WHAT DOES THE FUTURE HOLD?
Our goal when creating these GPTs is to go through the function
of ChatGPTs GPT Builder and provide an example of one of the
many possibilities AI, and this program in particular, have to offer.
The capabilities of AI have progressed and continue to progress
rapidly as its use has grown across various ﬁelds. One of the
main utilities of LLMs is their ability to increase efﬁciency and
simplify tasks that can be time-consuming. While existing search
engines grant researcher’s similar access to large libraries of
existing literature, the search process can often be tedious and
time-consuming. AI models that can be created, like Medi
Research Assistant, have the ability to collect various sources
and present them in a way that is speciﬁc to the user’s input. By
asking the GPT to provide summaries in a particular format with
speciﬁc information from each source it ﬁnds, users can more
efﬁciently decide which sources would be valuable to discuss in
their manuscripts.
As these programs improve we see that although they are
effective in assisting with time-consuming work, they are also
capable of creating high-quality work that takes more than just
time and effort. With the development of GPT agents, the future
of optimizing the irreplicable function of these programs is
endless. Users can now personalize these models to produce
what they want, and more importantly, how they want it in a
consistent manner that satisﬁes the user.
In medical literature speciﬁcally, these advances have opened
the doors to allow researchers to reduce the time it takes to
complete their projects that have been slowed down by the
process of writing. By expressing their research ideas, their
intended use of data and analyses, and their writing style and
points of emphasis, researchers can use the assistance of these
GPTs to advance their projects in a more tailored and timely
manner. This allows users to be more efﬁcient while also
remaining authentic and avoiding generic outputs to the extent
that the AI allows through personalized inputs and conﬁgurations.
As it stands, the use of generic programs, such as ChatGPT,
leads to the persistent production of work that is not reliable and
requires extensive amounts of effort and time to review.
Although the issues of fabricated data and plagiarism remain in
the early stages of creating personalized GPT’s, their ability to
create speciﬁc conﬁgurations that allow for consistent outputs is
what makes them unique in the realm of AI. By investing time in
the early processes of creating these GPTs to ensure reliable
products through a series of iterative commands, thorough and
complete fact-checking, and an overall review of their outputs
and respective workﬂow, custom GPTs are the next step in being
able to use AI programs in medical literature in a way that ad-
dresses several concerns that exist in current literature.
The question of AI authorship remains a point of contention in the
eyes of various journals and scientists as their function currently
stands.7,8 Tools such as ChatGPT’s GPT builder, and others that
may follow suit, can contribute to this discussion as they prove to
have more “original” work through the personalization of these
chatbots by the authors themselves. As the personalization of
different chatbots improves and their use becomes more
prevalent and accepted as the work of both the AI itself and
the user that conﬁgures the program, new conclusions may be
reached about the originality and resulting authorship policies
surrounding products of AI in scientiﬁc literature.
Figure 5. An example of one of the capabilities of Medi Research
Assistant as an additional GPT that specializes in literature review.
WORLD NEUROSURGERY 193: 461e468, JANUARY 2025
www.journals.elsevier.com/world-neurosurgery
465
TECHNICAL NOTE


## Page 6

The reader may ﬁnally wonder, was this paper itself a product
of the personalized GPT Neurosurgery Research Paper Writer?
Although the answer is no, as an exercise, the authors
inputted the sources that were used and the goal of this
manuscript into our custom GPT. The resulting manuscript is
provided as a Supplementary Material 1 online. We may be
inherently biased, even more so than our GPT, but human-
derived manuscripts remain to our eyes more detailed,
nuanced, and rigorous than our GPT’s efforts, at least for now.
The tremendous pace of innovation in this ﬁeld, however,
makes any prediction of the future utility of these tools a
particular challenge.
CRediT AUTHORSHIP CONTRIBUTION STATEMENT
Aymen Kabir: Writing e review & editing, Writing e original
draft, Supervision, Methodology, Investigation, Data curation,
Conceptualization. Suraj Shah: Writing e review & editing,
Writing e original draft, Methodology, Investigation, Formal
analysis, Data curation. Alexander Haddad: Writing e review &
editing,
Supervision,
Project
administration,
Methodology.
Daniel M.S. Raper: Writing e review & editing, Supervision,
Project
administration,
Methodology,
Investigation,
Conceptualization.
REFERENCES
1. Temsah O, Khan SA, Chaiah Y, et al. Overview of
early ChatGPT’s presence in medical literature:
insights
from
a
Hybrid
literature
review
by
ChatGPT and human experts. Cureus. 2023;15:
e37281.
2. Macdonald C, Adeloye D, Sheikh A, Rudan I. Can
ChatGPT draft a research article? An example of
population-level
vaccine
effectiveness
analysis.
J Glob Health. 2023;13:01003.
3. Giglio AD, Costa MUPD. The use of artiﬁcial in-
telligence to improve the scientiﬁc writing of non-
native English speakers. Rev Assoc Med Bras. 2023;69:
e20230560.
4. Májovský M, Cerný M, Kasal M, Komarc M,
Netuka D. Artiﬁcial intelligence can generate
fraudulent but authentic-looking scientiﬁc medical
articles: Pandora’s Box has been opened. J Med
Internet Res. 2023;25:e46924.
5. Elali FR, Rachid LN. AI-generated research paper
fabrication and plagiarism in the scientiﬁc com-
munity. Patterns (N Y). 2023;4:100706.
6. Gao
CA,
Howard
FM,
Markov
NS,
et
al.
Comparing
scientiﬁc
abstracts
generated
by
ChatGPT to real abstracts with detectors and
blinded human reviewers. NPJ Digit Med. 2023;6:
75.
7. Lee JY. Can an artiﬁcial intelligence chatbot be the
author of a scholarly article? J Educ Eval Health Prof.
2023;20:6.
8. Stokel-Walker C. ChatGPT listed as author on
research papers: many scientists disapprove. Na-
ture. 2023;613:620-621.
Conflict of interest statement: The authors declare that
the article content was composed in the absence of any
commercial or financial relationships that could be
construed as a potential conflict of interest.
Received 2 October 2024; accepted 14 October 2024
Citation: World Neurosurg. (2025) 193:461e468.
https://doi.org/10.1016/j.wneu.2024.10.041
Journal homepage: www.journals.elsevier.com/world-
neurosurgery
Available online: www.sciencedirect.com
1878-8750/ª 2025 The Authors. Published by Elsevier Inc.
This is an open access article under the CC BY license
(http://creativecommons.org/licenses/by/4.0/).
466
www.SCIENCEDIRECT.com
WORLD NEUROSURGERY, https://doi.org/10.1016/j.wneu.2024.10.041
TECHNICAL NOTE


## Page 7

SUPPLEMENTAL MATERIAL
This supplemental material is a manuscript with references
generated through the use of our GPTs, Neurosurgical Research
Paper Writer, and Medi Research Assistant.
INTRODUCTION
Artiﬁcial intelligence (AI), particularly in the form of large language
models (LLMs), has brought profound changes to scientiﬁc
research and literature. The advent of models like OpenAI’s GPT
series has demonstrated immense capabilities in automating
various tasks associated with scientiﬁc writing. These models are
capable of generating complex text, summarizing research, and
assisting with data analysis across a range of ﬁelds, including
medicine and neurosurgery.
In neurosurgery, where the interpretation of clinical data and
scientiﬁc writing demands high precision, AI offers unprece-
dented advantages. The ability to generate well-structured sci-
entiﬁc papers, analyze clinical trials, and interpret intricate
medical
terminology
helps
streamline
research
workﬂows.
However, the use of AI in this domain is not without controversy.
Early insights have shown that tools like ChatGPT can already be
found in medical literature, either assisting in research or being
used in some capacity in peer-reviewed papers.1 In fact, there
has
been
growing
interest
in
whether
AI
can
produce
scientiﬁcally rigorous articles on its own.2
One key advantage of LLMs like GPT-4 is their ability to aid non-
native English speakers in improving the quality of their scientiﬁc
writing, helping to break down language barriers that often
impede
global
scientiﬁc
collaboration.3
Furthermore,
these
models have the potential to democratize access to knowledge
by
processing
vast
amounts
of
literature,
offering
interpretations in multiple languages, and summarizing complex
medical studies for easier consumption.
Despite the excitement surrounding AI’s potential, there are
signiﬁcant concerns. Issues such as the generation of fabricated
or misleading information, as well as the temptation to misuse AI
for fraudulent academic purposes, have emerged as critical
ethical dilemmas. For example, AI models have demonstrated
the ability to create realistic yet entirely fabricated scientiﬁc ar-
ticles, raising alarms about their misuse in academic circles.4 As
a result, the use of AI in scientiﬁc writing remains a double-edged
sword, offering both incredible potential and signiﬁcant chal-
lenges that must be carefully managed.
Building Neurosurgical Research Paper Writer
The development of personalized GPT models, such as Neuro-
surgical Research Paper Writer, represents a major advancement
in AI-assisted content creation. Unlike generalized GPT models,
which are designed to handle a broad range of tasks, personal-
ized models are tailored to meet speciﬁc requirements. The
creation of Neurosurgical Research Paper Writer illustrates the
meticulous process of reﬁning an AI to meet the unique demands
of neurosurgical research.
The process began by identifying the speciﬁc requirements of
neurosurgical research, where accuracy and technical depth are
paramount. Neurosurgical literature involves highly specialized
terminology, clinical data, and the precise interpretation of
research ﬁndings. To build Neurosurgical Research Paper Writer,
the developers created a clear set of guidelines and instructions
that directed the model to focus on the structure and content
needed for scientiﬁc papers. These instructions included how to
synthesize data, analyze clinical trials, and meet strict word count
limits for each section of a research paper.
The training process involved feeding the model with neurosur-
gical literature, including peer-reviewed journals and clinical trial
reports. Over time, the model was ﬁne-tuned to recognize the
unique terminology used in neurosurgery, ensuring that it could
handle the highly technical language of the ﬁeld. However, the
initial outputs from the model were often too generic or lacking in
technical detail. This is a common challenge when building
personalized AI models, as they must be reﬁned through multiple
iterations of training and feedback.
One of the primary challenges during the development of
Neurosurgical Research Paper Writer was ensuring the accuracy
of the generated content. AI models, especially in highly
specialized ﬁelds, can struggle with generating reliable informa-
tion. To address this, Neurosurgical Research Paper Writer was
rigorously tested and reﬁned to minimize errors and ensure that
its outputs were based on veriﬁable data. This process helped to
avoid the pitfalls of AI-generated content, such as the creation of
fabricated information or hallucinated data, which is a known
issue with LLMs.4
A signiﬁcant feature of Neurosurgical Research Paper Writer is
its ability to follow strict academic guidelines, such as maintain-
ing appropriate section lengths and adhering to word count limits.
In scientiﬁc writing, particularly in peer-reviewed journals, main-
taining these standards is critical for publication. The developers
ensured that the model could generate outputs that were both
technically accurate and structured according to the speciﬁc
formatting requirements of neurosurgical research papers.
Additionally, Neurosurgical Research Paper Writer was designed
to handle the complex and detailed nature of neurosurgical
studies, often involving the synthesis of large amounts of clinical
data. This included not only summarizing the results of clinical
trials but also interpreting them in a way that adhered to the
standards of evidence-based medicine. By training the model on
high-quality, peer-reviewed sources, the developers ensured that
it could generate well-structured papers that reﬂected the latest
advancements in the ﬁeld.
Finally, the development of Neurosurgical Research Paper Writer
also highlights the broader implications of personalized GPT
models in academic research. By creating a model speciﬁcally
tailored to neurosurgical writing, the developers have demon-
strated how AI can be customized to meet the unique needs of
specialized ﬁelds. This personalization offers signiﬁcant potential
for enhancing the efﬁciency and accuracy of scientiﬁc writing,
reducing the time and effort required to draft complex papers
while ensuring that the content remains of high quality.
Building Medi Research Assistant
Given the overwhelming volume of scientiﬁc publications in
recent years, researchers often struggle to keep up with the
latest studies and articles related to their work. To address this
challenge, we developed the GPT, Medi Research Assistant, to
streamline the process of ﬁnding and summarizing relevant ac-
ademic sources.
WORLD NEUROSURGERY 193: 461e468, JANUARY 2025
www.journals.elsevier.com/world-neurosurgery
467
TECHNICAL NOTE


## Page 8

Medi Research Assistant is an advanced AI tool designed to
assist researchers by searching the web for academic sources
related to any research topic provided by the user. Once relevant
sources are identiﬁed, the tool generates concise summaries for
each article, allowing the user to quickly evaluate the relevance
and quality of the material without needing to read through each
paper in detail.
This tool is particularly valuable for researchers who need to
navigate large volumes of academic literature in a short period.
By providing comprehensive summaries alongside the original
sources, Medi Research Assistant simpliﬁes the literature review
process, enhancing efﬁciency and saving time. Additionally, the
tool’s ability to ﬁlter out less relevant or lower-quality studies
ensures that researchers can focus on high-impact work that is
directly related to their research topic.
Moreover, Medi Research Assistant addresses the issue of in-
formation overload, which has become increasingly problematic
with the exponential growth of scientiﬁc publications. By curating
only the most relevant sources, this tool enables researchers to
stay current with the latest developments in their ﬁeld without
being overwhelmed by the volume of available literature.
Challenges and Issues with GPTs in Scientific Literature
While AI models like Neurosurgical Research Paper Writer offer
substantial advantages in scientiﬁc writing, they also present
several challenges, particularly in the context of neurosurgical
research. One of the primary concerns is the potential for AI to
generate content that appears accurate but is, in fact, fabricated
or misleading. This issue, known as AI hallucination, occurs when
models produce plausible but false information. Such errors can
have serious consequences in scientiﬁc literature, where preci-
sion is critical.
In addition to hallucinations, there are concerns about the ethical
use of AI in academic research. AI-generated papers that fabri-
cate data or plagiarize from existing sources pose signiﬁcant risks
to the integrity of scientiﬁc literature.3,5 Fraudulent papers can
damage the credibility of academic journals and lead to the
dissemination of false information. Additionally, leading journals
have emphasized that AI-generated content, while useful as a
research tool, may not meet the criteria for authorship, as AI
lacks the ability to take responsibility for the work it produces.6,7
Moreover, while AI models like GPT-4 are powerful, they do not
possess a true understanding of the content they generate. This
lack of comprehension can result in superﬁcial analysis or
misinterpretation of complex medical data. Human oversight re-
mains crucial in reviewing and validating AI-generated content,
ensuring that it adheres to scientiﬁc rigor and ethical standards.
Despite these challenges, AI’s potential in neurosurgical research
is immense. As the technology improves, addressing these lim-
itations will be critical in realizing AI’s full potential in enhancing
research quality and productivity.
CONCLUSION
AI, especially through personalized models like Neurosurgical
Research Paper Writer, offers signiﬁcant potential in trans-
forming
neurosurgical
research.
By
automating
time-
consuming tasks such as literature review and data synthe-
sis, AI can increase productivity and accuracy in scientiﬁc
writing. This has been demonstrated in both neurosurgery and
other medical ﬁelds, where AI has already begun to play a
supporting role.7
However, the challenges posed by AI, including hallucinations,
ethical concerns, and the risk of data fabrication, highlight the
need for caution. The potential for AI-generated fraudulent pa-
pers is a serious issue that needs addressing through stronger
oversight and better AI training. Furthermore, human experts
must continue to play an essential role in validating and verifying
AI outputs to ensure that medical research remains reliable and
trustworthy.
In the future, as AI technology continues to evolve and address
its current limitations, it could become an indispensable tool for
researchers in neurosurgery and other specialized ﬁelds. Over-
coming these challenges will be key to unlocking AI’s full po-
tential and ensuring that it enhances, rather than undermines,
scientiﬁc research.
REFERENCES
1. Temsah O, Khan SA, Chaiah Y, et al. Overview of
Early ChatGPT’s Presence in Medical Literature:
Insights From a Hybrid Literature Review by
ChatGPT and Human Experts. Cureus. 2023;15:
e37281.
2. Elali FR, Rachid LN. AI-generated research paper
fabrication and plagiarism in the scientiﬁc com-
munity. Patterns (N.Y.). 2023;4:100706.
3. Giglio AD, Costa MUPD. The use of Artiﬁcial In-
telligence to Improve the Scientiﬁc Writing of Non-
Native English Speakers. Revista da Associacao Medica
Brasileira (1992). 2023;69:e20230560.
4. Májovský M, Cerný M, Kasal M, Komarc M,
Netuka D. Artiﬁcial Intelligence Can Generate
Fraudulent but Authentic-Looking Scientiﬁc Med-
ical Articles: Pandora’s Box Has Been Opened.
J Med Internet Res. 2023;25:e46924.
5. Macdonald C, Adeloye D, Sheikh A, Rudan I. Can
ChatGPT Draft a Research Article? An Example of
Population-Level Vaccine Effectiveness Analysis.
J Glob Health. 2023;13:e01003.
6. Lee JY. Can an Artiﬁcial Intelligence Chatbot be the
Author of a Scholarly Article? J Educ Eval Health Prof.
2023;20:6.
7. Stokel-Walker C. ChatGPT listed as author on
research papers: many scientists disapprove. Na-
ture. 2023;613:620-621.
468
www.SCIENCEDIRECT.com
WORLD NEUROSURGERY, https://doi.org/10.1016/j.wneu.2024.10.041
TECHNICAL NOTE


---

## Notes
- Auto-converted from PDF
- Please review and clean up formatting as needed
- Add manual annotations and summaries above this line
