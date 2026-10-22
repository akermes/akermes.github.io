#!/usr/bin/env python3
"""Generates the static portfolio site into ../build. All copy lives here."""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "..", "build")
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400;9..144,600;9..144,400,30;9..144,600,30&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">')

NAV = [("Work", "portfolio.html"), ("About", "about.html"), ("Work with me", "work-with-me.html"), ("Resume", "assets/Aaron_Kermes_Resume.pdf")]

def page(path, title, body, desc, current=None):
    depth = path.count("/")
    root = "../" * depth
    nav = "".join(
        f'<li><a href="{root}{href}"{" aria-current=\"page\"" if current == href else ""}{" target=\"_blank\" rel=\"noopener\"" if href.endswith(".pdf") else ""}>{label}</a></li>'
        for label, href in NAV)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{FONTS}
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="wordmark" href="{root}index.html">Aaron Kermes</a>
<nav aria-label="Main"><ul class="nav">{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div>Aaron Kermes, instructional designer. Show Low, Arizona, working remotely.</div>
<div><a href="mailto:akermes@outlook.com">akermes@outlook.com</a> &nbsp;|&nbsp; <a href="https://www.linkedin.com/in/aaron-kermes" rel="noopener">LinkedIn</a> &nbsp;|&nbsp; <a href="{root}assets/Aaron_Kermes_Resume.pdf">Resume (PDF)</a></div>
</div></footer>
</body>
</html>"""
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(doc)

# ---------------------------------------------------------------- projects
PROJECTS = [
 dict(slug="fnu-practice-module", title="Flexible Novel Unit Practice Module", pattern="Practice module, built in code",
      card="A 30-minute interactive module that replaced four hours of lecture. One HTML file, no authoring tool.",
      thumb="pearson/placeholder", thumb_override="../assets/img/fnu-watch-one.jpg",
      sub="A 30-minute interactive module that replaces four hours of lecture with practice.",
      body=[
       "My team was trained on a new content build process through four one-hour presentations with no chance to practice. The team was new to the process, and the errors that training was supposed to prevent are expensive: a wrong label or template means rework for the designer, the reviewer, and the vendor.",
       "I built a prototype practice module on my own initiative. It walks a designer through the process by doing it: a quick check on the rules, a worked example that reveals each markup decision in order, eight label-and-decide drills, a guided build where the learner chunks an activity into screens and gets feedback on every break, a peer review simulation with planted errors, and a one-page job aid with a checklist.",
       "It is a single HTML file with no dependencies: no authoring tool, no LMS, no login. It runs in any browser, supports dark mode, is keyboard accessible, and uses sample content so nothing proprietary is exposed.",
      ],
      cta=("Open the module", "../modules/fnu-practice-module.html"),
      spec=dict(type="Interactive eLearning, self-initiated", client="McGraw Hill (internal prototype)", date="October 2026",
                tools=["HTML", "CSS", "JavaScript"],
                skills=["Practice-based design", "Worked examples", "Feedback design", "Scenario and simulation design", "Job aid design", "Front-end development", "Accessibility"]),
      process=[
       ("Initial design", "I listed the decisions a designer makes in the process (chunk, label, template, page type, teach note placement, screenmap row) and the errors a peer reviewer is told to catch. Each one became a practice item."),
       ("Storyboarding", "The module follows a fixed arc: see it done, make single decisions, make the whole set of decisions, then judge someone else's. The job aid is what the learner keeps."),
       ("Development", "Hand-coded so the team could run it from a shared drive. Each step marks itself complete, feedback is immediate and specific to the choice made, and the guided build grades every screen break against a model answer."),
      ],
      finished_html='<p>The module is embedded below. The process and tool names belong to the client; the activity content is illustrative.</p>'
                    '<iframe class="embed" src="../modules/fnu-practice-module.html" title="Flexible Novel Unit practice module" loading="lazy"></iframe>'
                    '<p style="margin-top:12px"><a href="../modules/fnu-practice-module.html" target="_blank" rel="noopener">Open the module in its own tab</a></p>',
 ),
 dict(slug="pathways", wide=True, title="Pathways", pattern="AI-generated curriculum with built-in practice",
      card="A homeschool platform on the Claude API that turns a parent's goals into lessons, worksheets, and games. Live and in use.",
      thumb="pathways/generate-form.jpg",
      sub="An AI-powered homeschool platform that turns a parent's goals into a full K-12 curriculum.",
      body=[
       "A friend wanted to homeschool his kids but did not know how to build a curriculum, pick a teaching approach, or keep track of progress. Most tools either hand parents a rigid program or leave them to figure it out alone.",
       "I designed and built Pathways, a web app on the Claude API that generates full lessons from the parent's goals and the student's profile: objective, materials, vocabulary, aligned standards (Common Core, NGSS, and the family's state), a three-part activity sequence, a scored assessment, modifications for struggling and advanced learners, and homework. It supports six pedagogical models and blends them using a compatibility matrix I designed.",
       "The student side is where the practice happens. Every lesson generates its own Game Zone from the lesson's vocabulary: flashcards the student marks as known, and a match game that counts tries. Practice always matches what was just taught. Students see their own progress and grades; parents see gradebooks, transcripts, and progress by subject.",
      ],
      cta=("Try Pathways", "https://pathways2.netlify.app/"),
      spec=dict(type="Learning product design and development", client="Personal project, in use by families", date="2025 to present",
                tools=["Claude API", "React 18", "Vite", "Tailwind CSS", "Supabase", "Netlify Functions", "xAPI"],
                skills=["Learning product design", "Curriculum generation", "Prompt design", "Pedagogical model design", "Practice and feedback design", "Full-stack development"]),
      process=[
       ("Initial design", "I started with the parent's job to be done: decide what to teach, how, and whether it is working. Each of those became a part of the app. The six pedagogical models came first, on paper, with a matrix of which ones combine well."),
       ("Storyboarding", "I storyboarded the parent flow and the student flow separately, since they need different voices and different controls. The prompts were drafted as part of the storyboard, with the content each screen needed to show."),
       ("Development", "Built in React with Supabase for data and Netlify serverless functions calling the Claude API. I shipped it in increments: curriculum generation first, then the student portal and games, then worksheets, gradebooks, and transcripts."),
      ],
      gallery=[
       ("pathways/generate-form.jpg", "The generator reads the student's profile: learning style, pace, interests, accommodations, and the state standards to layer on top of Common Core."),
       ("pathways/lifesci-lesson-parent-top.jpg", "A generated Grade 12 life science lab, parent view: objective, materials, and vocabulary."),
       ("pathways/lesson-activities-assessment.jpg", "Every lesson has a three-part activity sequence and a scored assessment that can be added to the gradebook."),
       ("pathways/lifesci-lesson-student-top.jpg", "The same lesson in the student's voice."),
       ("pathways/lifesci-flashcards.jpg", "Game Zone: flashcards generated from the lesson's vocabulary."),
       ("pathways/lifesci-match-3of6.jpg", "The match game counts tries, so a student can see the difference between knowing and guessing."),
       ("pathways/student-grades.jpg", "Students see their own grades, GPA, and credits."),
       ("pathways/kathleen-profile-progress.jpg", "Parents see progress by subject for each student."),
      ],
 ),
 dict(slug="data-literacy", title="Data Literacy for Individual Contributors", pattern="Scenario-based activities",
      card="Scenario activities built around charts generated in code, for a corporate training client. Observation to inference to decision.",
      thumb="bundle/customer-feedback-dip.jpg",
      sub="Scenario-based activities that teach people to read a chart before they act on it.",
      body=[
       "Individual contributors see dashboards every day and are expected to draw conclusions from them. Most have never been taught how. The client needed a data literacy program that fit inside its existing learning series and matched its brand.",
       "I designed a set of concept slides (trends, gaps, cyclical and outlier patterns, scatter plots, pie charts) and a series of scenario-based activities. Each activity gives the learner a chart with a realistic business situation (a dip in customer satisfaction, equipment downtime by shift, AI chatbot resolution rates) and a sequence of questions that walks them from observation to inference to a recommendation.",
       "Every chart was generated in code so the data told the story I needed it to and the palette stayed consistent across the series. For the same client I also designed the Transformational Leadership session and the Critical Thinking for Managers learning plan, which I adapted for three more audiences. That work is under NDA, so it is described here and not shown. A trainer who delivered Transformational Leadership called it the best experience she has had as a trainer.",
      ],
      cta=None,
      spec=dict(type="Instructor-led and self-paced training design", client="Bundle, through The Learning Loop", date="2026",
                tools=["PowerPoint", "Python (matplotlib) for the charts"],
                skills=["Scenario design", "Data visualization", "Question sequencing", "Brand-consistent slide design", "Audience adaptation"]),
      process=[
       ("The need", "Learners could describe a chart but not act on it. The gap was the step from \"the line goes down\" to \"here is what I would do next.\""),
       ("What I delivered", "Concept slides that teach one pattern each, and activity slides that put the learner in a situation and ask for a decision. Both sets follow the client's template so a facilitator can drop them into any session."),
       ("Development", "Charts built in matplotlib with a fixed palette and annotation style, placed into the client's slide template, with the question sequence written to move from what the chart shows to what the learner should do."),
      ],
      gallery=[
       ("bundle/customer-feedback-dip.jpg", "Activity: a dip in customer feedback. What happened in April, and what would you check first?"),
       ("bundle/revenue-by-product.jpg", "Activity: three product lines, three different stories. Where would you focus the team?"),
       ("bundle/ai-resolution-rates.jpg", "Activity: AI resolution rises while escalations fall. What is the satisfaction score telling you?"),
       ("bundle/downtime-by-shift.jpg", "Activity: night shift shows 40% more downtime. What questions come before a conclusion?"),
       ("bundle/inventory-vs-demand.jpg", "Activity: demand spikes faster than inventory. When should ordering change?"),
       ("bundle/gap-pattern.jpg", "Concept: a gap pattern, a sudden drop to zero."),
       ("bundle/seasonal-outlier.jpg", "Concept: a repeating seasonal pattern with one outlier."),
       ("bundle/trend-direction.jpg", "Concept: upward, downward, and sideways trends."),
       ("bundle/tenure-vs-rating.jpg", "Concept: a scatter plot with two outliers worth asking about."),
       ("bundle/time-allocation.jpg", "Concept: parts of a whole."),
      ],
 ),
 dict(slug="sales-training-evaluation", title="Consultative Sales Training and Evaluation", pattern="Evaluation design, Kirkpatrick levels 1 to 4",
      card="A coaching program with measured results: shorter calls, more calls, and a 15% lift in enrollments.",
      thumb="results",
      sub="A coaching program with measured results: shorter calls, more calls, more enrollments.",
      body=[
       "Enrollment advisors were spending too long on calls that went nowhere. Leads sat in the pipeline, and conversion rates were flat.",
       "As the team's manager, I ran a consultative sales training program in Mindtickle and built the evaluation around it: scored role-plays, QA-scored call recordings against a rubric, and dashboards in Tableau that tied the two together.",
       "The evaluation results drove focused call coaching. Call length dropped 17%, call volume rose 12%, stale leads left the pipeline sooner, and team enrollments increased 15%. I reported KPIs, growth areas, and an improvement plan with targets to leadership.",
      ],
      cta=None,
      spec=dict(type="Training program and evaluation", client="Pearson, Student Recruitment Services (supporting Arizona State University Online)", date="2018 to 2021",
                tools=["Mindtickle", "Tableau", "Power BI", "Salesforce"],
                skills=["Evaluation design", "Kirkpatrick levels 1 through 4", "Rubric design", "Call coaching", "Data visualization", "Leadership reporting"]),
      process=[
       ("Initial design", "I wrote an evaluation plan before the training ran: what we would measure, how, and what good looked like. That meant the training had a target, not just a completion date."),
       ("Storyboarding", "The rubric was the storyboard. It defined the behaviors we wanted on calls, which shaped both the Mindtickle content and the QA scoring."),
       ("Development", "Training ran in Mindtickle. Role-plays and recorded calls were scored, the scores fed the Tableau dashboard, and the dashboard drove weekly coaching. The cycle repeated until the numbers moved."),
      ],
      finished_html="""<p>Results for a team of 22 enrollment advisors, measured before and after the coaching cycle.</p>
<ul class="results">
<li><div class="num">17%</div><div class="what">shorter average call length</div></li>
<li><div class="num">12%</div><div class="what">more call volume</div></li>
<li><div class="num">15%</div><div class="what">increase in team enrollments</div></li>
</ul>
<table><thead><tr><th>Kirkpatrick level</th><th>What was measured</th><th>How</th></tr></thead><tbody>
<tr><td>1. Reaction</td><td>Advisor response to the program</td><td>Post-training survey</td></tr>
<tr><td>2. Learning</td><td>Consultative skills demonstrated</td><td>Scored role-plays with advisors and managers</td></tr>
<tr><td>3. Behavior</td><td>Skills used on real calls</td><td>QA team scored recorded calls against a rubric; results drove weekly coaching</td></tr>
<tr><td>4. Results</td><td>Call length, call volume, pipeline health, enrollments</td><td>Tableau dashboards reported to leadership with an improvement plan and targets</td></tr>
</tbody></table>""",
 ),
 dict(slug="graduate-interactives", title="Graduate Cybersecurity and Nursing Interactives", pattern="Branching scenarios and case studies",
      card="30+ scenario-based modules for three universities: decision trees, patient cases, practice hubs.",
      thumb="pearson/nmap-tree.jpg",
      sub="Scenario-based practice for graduate students who need to make decisions, not memorize facts.",
      body=[
       "Graduate nursing and cybersecurity students learn by working cases: a patient with chest pain, a network that needs scanning. Reading about it is not the same as deciding what to do next.",
       "At Pearson Online Learning Services I designed and built 30+ interactive modules for the Master of Science in Cyber Security at the University of North Dakota and the Master of Science in Nursing programs at Maryville University and Regis College. The formats match the thinking each field requires: branching decision trees for Nmap scanning options with feedback on every choice, patient case scenarios with video introductions and transcripts, anatomy practice hubs, and practical guides such as prescription writing and policy briefs.",
       "Every module was built as a self-contained web module loaded into Canvas, with faculty subject matter experts, and course revisions were driven by LMS analytics and end-of-course evaluations term over term.",
      ],
      cta=("Open the Nmap Scanning Tree", "https://lmscontent.embanet.com/Media/UND/CSCI587/CSCI587-w03-m01/"),
      spec=dict(type="Interactive eLearning for higher education", client="Pearson Online Learning Services, for UND, Maryville, and Regis", date="2021 to 2023",
                tools=["HTML", "CSS", "JavaScript", "Canvas LMS", "Articulate 360", "Camtasia"],
                skills=["Scenario design", "Branching logic", "Case study writing", "SME collaboration", "Accessibility (transcripts, keyboard navigation)", "LMS integration"]),
      process=[
       ("Course map", "Every course started with the faculty subject matter expert and me completing and aligning on the course map: outcomes, weekly topics, assessments, and where interactive practice was needed."),
       ("Lesson design document", "Each week was planned in a lesson design document that placed readings, media, activities, and assessment against the week's objectives."),
       ("Storyboard and build", "Each scenario and media piece was storyboarded screen by screen before build: on-screen text, choices, feedback, and where each choice leads. The Nmap Scanning Tree storyboard is reconstructed below from the shipped module."),
      ],
      finished_html="""<p>Eight of the modules, live. Each opens in a new tab.</p>
<ul class="gallery">
<li><figure><a href="https://lmscontent.embanet.com/Media/UND/CSCI587/CSCI587-w03-m01/" target="_blank" rel="noopener"><img src="../assets/img/pearson/nmap-tree.jpg" alt="Nmap Scanning Tree: a branching decision tree with four scan type options"></a><figcaption>Nmap Scanning Tree (UND). Four decisions in sequence, feedback on every option, no dead ends.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/MVU/NURS611/NURS611-w15-m02/" target="_blank" rel="noopener"><img src="../assets/img/pearson/integumentary-cases.jpg" alt="Integumentary System Case Studies: choose one of four patients"></a><figcaption>Integumentary System Case Studies (Maryville). Four patients, a branching diagnosis path for each, and a printable summary.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/MVU/NURS611/NURS611-w02-m01/" target="_blank" rel="noopener"><img src="../assets/img/pearson/chest-pain-intro.jpg" alt="Chest Pain Scenario introduction with a patient video and transcript link"></a><figcaption>Chest Pain Scenario (Maryville). Video patient intro with transcript, then a stepped case.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/RC/NU664A/NU664A-w06-m03/" target="_blank" rel="noopener"><img src="../assets/img/pearson/prescription-writing-lesson.jpg" alt="Prescription Writing lesson with patient case tiles"></a><figcaption>Prescription Writing (Regis). A multi-patient pediatric lesson with a check-your-understanding section.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/MVU/NURS602/NURS602-w04-m02/" target="_blank" rel="noopener"><img src="../assets/img/pearson/access-to-care.jpg" alt="Access to Care Case Study with a timeline of tabs"></a><figcaption>Access to Care Case Study (Maryville). One patient's story told across a timeline.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/UND/CSCI587/CSCI587-w06-m02/" target="_blank" rel="noopener"><img src="../assets/img/pearson/social-eng-video.jpg" alt="Social Engineering Scenarios video module"></a><figcaption>Social Engineering Scenarios (UND). Video-based attack recognition.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/UND/CSCI587/CSCI587-w08-m01/" target="_blank" rel="noopener"><img src="../assets/img/pearson/vuln-stack-layers.jpg" alt="Layers of the Vulnerability Stack interactive diagram"></a><figcaption>Layers of the Vulnerability Stack (UND). An interactive layered model.</figcaption></figure></li>
<li><figure><a href="https://lmscontent.embanet.com/Media/MVU/NURS612/NURS612-w11-m01/" target="_blank" rel="noopener"><img src="../assets/img/pearson/neurology-practice.jpg" alt="Neurology Practice hub with seven topic tiles"></a><figcaption>Neurology Practice (Maryville). A seven-topic practice hub with a printable study summary.</figcaption></figure></li>
</ul>
<h3 style="margin-top:36px">Reconstructed storyboard: Nmap Scanning Tree</h3>
<p>The original design documents for these modules are not available, so this one was rebuilt from the shipped module. Every prompt, choice, and feedback line below is quoted from the live activity.</p>
<p>Scenario: scan all TCP ports on a large network in as short a time as possible. Four decisions in sequence. In rows 1 to 3 one option is best and the others return feedback and keep the student in the row. Row 4 has no wrong answer; the activity completes once all three flags are reviewed.</p>
<table><thead><tr><th>Decision</th><th>Options</th><th>Best choice and why</th></tr></thead><tbody>
<tr><td>1. Scan type</td><td>-sT, -sV, -sS, -sC</td><td>-sS. "Syn scans, also known as stealth scans, take the shortest amount of time because they do not complete the three-way handshake."</td></tr>
<tr><td>2. Port range</td><td>-p-, -F, (no flag), -p 1-1000</td><td>-p-. "The -p- flag is shorthand for -p 1-65535. This flag tells Nmap to perform a scan on all TCP ports."</td></tr>
<tr><td>3. Timing</td><td>-T0 through -T5</td><td>-T4. Aggressive mode: fast without flooding a production network. -T5 "could flood the network with scanning traffic."</td></tr>
<tr><td>4. Output and input</td><td>--open, -oA, -iL</td><td>All three are good practice; the student reviews each.</td></tr>
</tbody></table>
<p>Feedback design: every option names the mechanism (handshake, port count, wait time) and either confirms the choice or redirects with "Select another option." Wrong choices never end the activity.</p>""",
 ),
 dict(slug="course-blueprints", title="Course Blueprints", pattern="Course-level design and localization",
      card="Course design for a university graduate course and the Canadian localization of a 26-lesson continuing ed course.",
      thumb="blueprint",
      sub="Course-level design documents that let a whole team build in the same direction.",
      body=[
       "Before a course is built, someone has to decide what it covers, what it leaves out, how it is assessed, and what has to change from the version that already exists. That document is the blueprint, and it is where most course problems are either prevented or created.",
       "Through Lumina Datamatics, I have written blueprints for two very different clients. For Western Governors University, I co-authored the course design for Cloud Strategy, a three-unit graduate course in the MSIT program, defining scope, out-of-scope boundaries, and the strategic (not technical) framing of every topic. For Cengage's ed2go, I am the Learning Designer on the Canadian localization of a 26-lesson Physiotherapy Assistant course: course description, outcomes, objectives, global edits, and a page-level revision tracker for every lesson.",
       "Both blueprints run through a structured review with a subject matter expert and an education specialist. My job is to make the first call on every item, document the reasoning, and leave a trail the client can approve line by line.",
      ],
      cta=None,
      spec=dict(type="Curriculum design and localization", client="Western Governors University and Cengage/ed2go, through Lumina Datamatics", date="2026",
                tools=["Word", "Excel", "Client blueprint templates"],
                skills=["Course analysis", "Outcome and objective writing", "Scope definition", "Localization", "SME collaboration", "Revision tracking"]),
      process=[
       ("Course analysis", "Each blueprint starts with a course analysis: what exists, what the client's standards require, and what the gap is. For the localization, that meant reading all 26 lessons against Canadian scope of practice, terminology, and regulatory references."),
       ("The blueprint as storyboard", "The template is the storyboard: course metadata, build instructions, in and out of scope, outcomes and objectives, then lesson-by-lesson revision rows with a category and a rationale."),
       ("Review", "Review runs in a fixed order (learning designer, subject matter expert, education specialist), and every row carries approvals from each. Nothing moves to build until the trail is complete."),
      ],
      finished_html="""<p>Excerpts from the two blueprints, with team names removed.</p>
<h3>Cloud Strategy (WGU, MSIT): scope definition</h3>
<p class="sub">Three competency units. Project-assessed. The course is strictly strategic: learners are not expected to set up cloud solutions, but must understand cloud infrastructure well enough to recommend a business strategy.</p>
<table><thead><tr><th>In scope</th><th>Out of scope</th></tr></thead><tbody>
<tr><td>Introduction to cloud computing; cloud economics; providers and ecosystems; architecture; security and compliance; migration strategies; managing cloud operations; governance; disaster recovery and business continuity</td><td>Deep technical training and hands-on configuration of cloud tools</td></tr>
</tbody></table>
<h3>Physiotherapy Assistant (ed2go): global course edits</h3>
<p class="sub">Course-wide principles agreed before any lesson-level work, each with the learning designer's note, the SME's response, the education specialist's note, and an approval.</p>
<table><thead><tr><th>Global edit</th><th>Decision</th></tr></thead><tbody>
<tr><td>Revise all writing to reflect Canadian spelling and grammar</td><td>Apply course-wide</td></tr>
<tr><td>Revise all language related to certification</td><td>Retain as the course-wide principle pending the client's decision between two certification options</td></tr>
<tr><td>Revise all language regarding governing bodies</td><td>Retain as a principle; resolve lesson by lesson, no global find-and-replace</td></tr>
<tr><td>Fact check all revised language against Canadian sources</td><td>Retain as a process requirement</td></tr>
<tr><td>Review and revise imagery and proper nouns for a Canadian context</td><td>Apply a Canadian standard to imagery and names</td></tr>
</tbody></table>
<p>The lesson-level tracker that follows carries one row per page element for each of the 26 lessons, with a revision category, the proposed change, and the alignment to the revised objectives.</p>""",
 ),
]

def project_page(p, prev_p, next_p):
    spec = p["spec"]
    tools = "".join(f"<li>{t}</li>" for t in spec["tools"])
    skills = "".join(f"<li>{s}</li>" for s in spec["skills"])
    body = "".join(f"<p>{b}</p>" for b in p["body"])
    cta = f'<p class="actions"><a class="btn" href="{p["cta"][1]}"{" target=\"_blank\" rel=\"noopener\"" if p["cta"][1].startswith("http") else ""}>{p["cta"][0]}</a></p>' if p.get("cta") else ""
    process = "".join(f"<h3>{h}</h3><p>{t}</p>" for h, t in p["process"])
    if p.get("gallery"):
        finished = f'<ul class="gallery{" wide" if p.get("wide") else ""}">' + "".join(
            f'<li><figure><img src="../assets/img/{src}" alt="{html.escape(cap)}" loading="lazy"><figcaption>{cap}</figcaption></figure></li>'
            for src, cap in p["gallery"]) + "</ul>"
    else:
        finished = p["finished_html"]
    pager = (f'<a href="{prev_p["slug"]}.html">Previous: {prev_p["title"]}</a>' if prev_p else "<span></span>") + \
            (f'<a href="{next_p["slug"]}.html">Next: {next_p["title"]}</a>' if next_p else "")
    html_body = f"""
<div class="project-hero"><div class="wrap">
<p class="crumb"><a href="../portfolio.html">Work</a> / {p["title"]}</p>
<h1>{p["title"]}</h1>
<p class="lede">{p["sub"]}</p>
</div></div>
<section style="padding-top:0"><div class="wrap project">
<div>{body}{cta}</div>
<dl class="spec">
<dt>Type</dt><dd>{spec["type"]}</dd>
<dt>Client</dt><dd>{spec["client"]}</dd>
<dt>Date</dt><dd>{spec["date"]}</dd>
<dt>Tools</dt><dd><ul>{tools}</ul></dd>
<dt>Skills</dt><dd><ul>{skills}</ul></dd>
</dl>
</div></section>
<section class="process"><div class="wrap"><h2>The design process</h2>{process}</div></section>
<section><div class="wrap"><h2>The finished project</h2>{finished}
<div class="pager">{pager}</div>
</div></section>
"""
    page(f"projects/{p['slug']}.html", f"{p['title']}: Aaron Kermes", html_body, p["sub"], current="portfolio.html")

def card_html(p, root=""):
    if p["thumb"] == "results":
        thumb = ('<div class="thumb" style="display:flex;align-items:center;justify-content:center;gap:18px;padding:16px">'
                 '<span style="font-family:var(--display);font-size:2.6rem;font-weight:600;color:var(--green)">17%</span>'
                 '<span style="font-family:var(--display);font-size:2.6rem;font-weight:600;color:var(--green)">12%</span>'
                 '<span style="font-family:var(--display);font-size:2.6rem;font-weight:600;color:var(--green)">15%</span></div>')
    elif p["thumb"] == "blueprint":
        thumb = ('<div class="thumb" style="display:flex;align-items:center;padding:20px">'
                 '<span style="font-family:var(--display);font-size:1.5rem;line-height:1.25;color:var(--green)">Course map, lesson design doc, revision tracker: 26 lessons, line by line.</span></div>')
    elif p.get("thumb_override"):
        thumb = f'<div class="thumb"><img src="{root}assets/img/fnu-watch-one.jpg" alt="" loading="lazy"></div>'
    else:
        thumb = f'<div class="thumb"><img src="{root}assets/img/{p["thumb"]}" alt="" loading="lazy"></div>'
    return f'<li class="card"><a href="{root}projects/{p["slug"]}.html">{thumb}<div class="pattern">{p["pattern"]}</div><h3>{p["title"]}</h3><p>{p["card"]}</p></a></li>'

# ---------------------------------------------------------------- pages
cards_home = "".join(card_html(p) for p in PROJECTS[:3])
cards_all = "".join(card_html(p) for p in PROJECTS)

HOME = f"""
<div class="hero"><div class="wrap">
<div>
<h1>Hi, I'm Aaron Kermes.</h1>
<p class="lede">I design learning that people can actually use.</p>
<p>Instructional designer with 13 years across corporate, higher education, and K-12 learning. I build the whole thing: analysis, curriculum, eLearning, instructor-led materials, the LMS, and the evaluation that shows whether it worked. Sometimes I build the tool, too.</p>
<p class="actions"><a class="btn" href="portfolio.html">See my work</a><a class="btn quiet" href="about.html">About me</a></p>
</div>
<img src="assets/img/aaron-kermes.jpg" alt="Aaron Kermes" width="380" height="380">
</div></div>

<section><div class="wrap">
<div class="section-head"><h2>Selected work</h2><a href="portfolio.html">All six projects</a></div>
<ul class="cards">{cards_home}</ul>
</div></section>

<section><div class="wrap teaser">
<div>
<h2>Who am I?</h2>
<p>I started in the classroom teaching high school English. I stayed in learning because I like solving the problems behind it. Since then I have managed a recruitment team, run tools and automation for a support organization, designed graduate courses for three universities, and built an AI learning platform on my own.</p>
<p>Along the way I kept finding the same thing: most training problems are design problems. That is the work I do now.</p>
<p><a href="about.html">Learn more about me</a></p>
</div>
<div>
<h2>Need a hand on a project?</h2>
<p>I take on contract instructional design work through The Learning Loop: course builds, curriculum blueprints, SME review cycles, LMS setup, and evaluation plans. Fixed scope, clear timelines, and deliverables your team can maintain after I'm gone.</p>
<div class="quote"><blockquote>"The best experience she's had as a trainer."</blockquote><p class="who">Feedback on a session I designed, relayed by Bundle's Learning Design Manager</p></div>
<p><a href="work-with-me.html">See how I work</a></p>
</div>
</div></section>
"""
page("index.html", "Aaron Kermes: Instructional Designer", HOME, "Aaron Kermes designs learning that people can actually use: corporate training, higher education courses, K-12 curriculum, and AI-powered learning tools.", current="index.html")

ABOUT = """
<div class="project-hero"><div class="wrap">
<h1>About me</h1>
<p class="lede">Teacher, manager, builder. Instructional designer by choice.</p>
</div></div>
<section style="padding-top:0"><div class="wrap about-grid">
<div>
<h2>I've spent 13 years in learning, on both sides of the desk.</h2>
<p>I started as a high school English teacher. I led a professional learning community, chaired my department, and ran professional development for other teachers. I learned to use assessment data to decide what to teach next, and I learned that good materials make good teaching easier.</p>
<p>At Pearson I managed a recruitment team of about 22 people. I was the hiring manager, ran onboarding and coaching, and built the Tableau and Power BI dashboards we used to track performance. When I finished my M.Ed. in Learning Design and Technologies at Arizona State, I moved into instructional design and built 30+ graduate modules in Canvas for nursing and cybersecurity programs. Later I managed tools and automation for a support organization, where I served as the unofficial product owner and ran a Microsoft Copilot adoption pilot that cut handling time by 42%.</p>
<p>Today I design Grade 9 literacy content for McGraw Hill's Summit! and Soar! program and run The Learning Loop, where I take on contract design work for companies and universities. On the side I built Pathways, an AI-powered homeschool platform on the Claude API. I work in ADDIE, SAM, and Agile, and I measure what I build.</p>
<p>I live in the White Mountains of Arizona and work remotely.</p>
<p class="actions"><a class="btn" href="https://www.linkedin.com/in/aaron-kermes" rel="noopener">Connect on LinkedIn</a><a class="btn quiet" href="assets/Aaron_Kermes_Resume.pdf">Download my resume</a></p>
</div>
<div>
<img src="assets/img/aaron-kermes.jpg" alt="Aaron Kermes" width="300" height="300">
<dl class="spec" style="margin-top:24px">
<dt>Education</dt><dd>M.Ed., Learning Design and Technologies, Arizona State University, 2020</dd><dd>B.A., Secondary Education (English), Arizona State University, 2012</dd>
<dt>Based in</dt><dd>Show Low, Arizona (remote)</dd>
</dl>
</div>
</div></section>
<section><div class="wrap">
<h2>Skills</h2>
<ul class="skills">
<li><strong>Learning design</strong><span>ADDIE, SAM, Agile, action mapping, scenario-based learning, curriculum blueprints and localization, learning objectives and assessment design, facilitator guides, WCAG 2.2 AA</span></li>
<li><strong>Development</strong><span>Articulate 360, Camtasia, Canva, Figma, HTML, CSS, JavaScript, React, PowerPoint</span></li>
<li><strong>Measurement</strong><span>Kirkpatrick, evaluation plans, LMS analytics, surveys and focus groups, Tableau, Power BI</span></li>
<li><strong>AI and automation</strong><span>Claude API, prompt workflow design, Microsoft Copilot, RPA, VBA, Python</span></li>
<li><strong>Platforms</strong><span>Canvas, Blackboard, Moodle, HealthStream, SharePoint, Smartsheet, Jira, Asana, Salesforce, Mindtickle, SCORM, AICC, xAPI</span></li>
</ul>
</div></section>
"""
page("about.html", "About Aaron Kermes", ABOUT, "Aaron Kermes: 13 years in learning as a teacher, manager, instructional designer, and builder.", current="about.html")

PORTFOLIO = f"""
<div class="project-hero"><div class="wrap">
<h1>Work</h1>
<p class="lede">Six projects that show how I work.</p>
<p>Each one demonstrates a different design pattern. Open any project for the problem, what I built, the process, and the finished piece.</p>
</div></div>
<section style="padding-top:8px"><div class="wrap">
<ul class="cards">{cards_all}</ul>
</div></section>
"""
page("portfolio.html", "Work: Aaron Kermes", PORTFOLIO, "Six instructional design projects by Aaron Kermes: practice modules, AI-generated curriculum, scenario activities, evaluation design, branching cases, and course blueprints.", current="portfolio.html")

WORK = """
<div class="project-hero"><div class="wrap">
<h1>Work with me</h1>
<p class="lede">Contract instructional design through The Learning Loop.</p>
</div></div>
<section style="padding-top:0"><div class="wrap teaser">
<div>
<h2>What I take on</h2>
<ul>
<li>Course and module builds (Articulate, Canvas, Moodle, HealthStream)</li>
<li>Curriculum blueprints and localization</li>
<li>Learning plans and facilitator materials for instructor-led training</li>
<li>SME review and comment resolution</li>
<li>LMS setup and administration</li>
<li>Evaluation plans and reporting</li>
</ul>
<h2 style="margin-top:32px">How a project runs</h2>
<p>We start with a short scoping call and I send back a written scope, timeline, and price. I work in defined review rounds, so you always know where the project stands. Everything I hand off is documented so your team can maintain it without me.</p>
<p class="actions"><a class="btn" href="mailto:akermes@outlook.com?subject=Project%20inquiry">Email me about your project</a></p>
</div>
<div>
<h2>Who I have worked with</h2>
<ul class="clients">
<li>McGraw Hill</li><li>Pearson</li><li>Cengage (ed2go)</li><li>Western Governors University</li><li>University of North Dakota</li><li>Regis College</li><li>Maryville University</li><li>Lumina Datamatics</li><li>Summit Healthcare</li><li>Bundle</li>
</ul>
<div class="quote" style="margin-top:32px">
<blockquote>"Hillary shared how much she loves Bundle. She's worked with other vendors before and said our curriculum is excellent, we make sure everything is easy, and the support we provide is top notch. She shared this is the best experience she's had as a trainer."</blockquote>
<p class="who">Feedback relayed by Melissa Johnson, Learning Design Manager at Bundle, after a trainer delivered the Transformational Leadership session I designed.</p>
</div>
</div>
</div></section>
"""
page("work-with-me.html", "Work with Aaron Kermes", WORK, "Contract instructional design through The Learning Loop: course builds, blueprints, SME review, LMS setup, and evaluation.", current="work-with-me.html")

for i, p in enumerate(PROJECTS):
    project_page(p, PROJECTS[i-1] if i > 0 else None, PROJECTS[i+1] if i < len(PROJECTS)-1 else None)

# housekeeping files
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "README.md"), "w").write("# akermes.github.io\n\nPortfolio site for Aaron Kermes. Plain HTML and CSS, no build step. GitHub Pages serves it as is (`.nojekyll` disables Jekyll).\n\nPages are generated from `gen/build_site.py`; edit the copy there or edit the HTML directly.\n")
print("built", len(PROJECTS), "project pages")
