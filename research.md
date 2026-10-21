---
title: Research
permalink: /research/
description: Publications, advanced working papers, and the CLAIMAX research project by Umut Yüksel.
---
<header class="page-heading"><p class="eyebrow">Research</p><h1>Research</h1></header>

<div class="research-intro" markdown="1">
{% assign projects = site.projects | sort: 'order' %}
{% for project in projects %}
{{ project.content | markdownify }}
{% endfor %}

More generally, my research lies at the intersection of international security, international law, and domestic politics. I rely on original data to examine the determinants of state claims and disputes, focusing on domestic political institutions and international law.
</div>

<nav class="section-nav" aria-label="Research sections"><a href="#publications">Publications</a><a href="#working-papers">Working papers</a></nav>

<section class="research-section" aria-labelledby="publications">
  <div class="section-label"><h2 id="publications">Publications</h2></div>
  <ol class="publication-list">
    {% for item in site.data.publications %}
    {% include publication.html item=item %}
    {% endfor %}
  </ol>
</section>

<section class="research-section" aria-labelledby="working-papers">
  <div class="section-label"><h2 id="working-papers">Advanced working papers</h2></div>
  <div>
    <ul class="publication-list">
      {% for item in site.data.working_papers %}
      <li class="publication"><h3>{{ item.title | escape }}</h3><p class="coauthors">With {{ item.coauthors | escape }}</p></li>
      {% endfor %}
    </ul>
    <p class="draft-note">Please feel free to <a href="mailto:{{ site.data.profile.email }}">contact me</a> for a copy of the latest drafts.</p>
  </div>
</section>
