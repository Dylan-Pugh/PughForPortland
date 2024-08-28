---
html_theme.sidebar_secondary.remove:
---

<!-- CSS overrides on the homepage only -->
<style>
.bd-container {
  background-color: rgb(37, 44, 99);
}

.bd-main .bd-content .bd-article-container {
  max-width: 80rem; */
}

.bd-article {
  color: white;
}
/* Extra top/bottom padding to the sections */
article.bd-article section {
  padding: 3rem 0 7rem; 
}
/* Override all h1 headers except for the hidden ones */
h1:not(.sd-d-none) {
  font-weight: bold;
  font-size: 48px;
  text-align: center;
  margin-bottom: 2rem;
}
/* Override all h3 headers that are not in hero */
h3:not(#hero h3) {
  font-weight: bold;
  text-align: center;
  color: white;
}

</style>

<!-- (homepage)= -->

<div id="hero">

<div id="hero-left">  <!-- Start Hero Left -->
  <img src="_static/logos/DylanPugh_Logo-03.png">
  <h3 style="font-weight: bold; margin-top: 10; color:white;">A progressive voice for Portland</h3>
  <p style="color:white;">I believe there is a place for empathy, compassion, and creativity in our political system, and I would be honored to bring these values to Augusta as your representative.</p>
</div>  <!-- End Hero Left -->

<div id="hero-right">  <!-- Start Hero Right -->

:::{card}
:img-background: _static/hero_portrait.png
:img-alt: Dylan Pugh photo
:margin: auto
:class-card: hero-image
:::

</div>  <!-- End Hero Right -->
</div>  <!-- End Hero -->

<hr class="rounded">

<!-- Keep in markdown to generate headerlink -->
# Core Issues
:::::{grid} 1 1 2 2
:gutter: 5

::::{grid-item-card}
:shadow: none
:class-card: sd-border-0

<div style="text-align: center;">
  <h4><strong>Affordable Housing</strong></h4><br/>
</div>
Building more is absolutely essential, but we also need to critically examine the ownership structure of existing housing stock. While the commoditization of housing may be normal, it is neither just, nor inevitable. We must have the courage to explore alternatives and ensure that everyone can live here with dignity.
::::

::::{grid-item-card}
:shadow: none
:class-card: sd-border-0

<div style="text-align: center;">
  <h4><strong>Economic Justice</strong></h4><br/>
</div>
Making Portland affordable isn’t just about lowering costs: we also need to increase wages, job security, and worker power. As a former small business owner, I know the risks and complexities of entrepreneurship well, and I am committed to supporting local businesses. We can meet this challenge and increase the wealth, stability, and diversity of our community.
::::

::::{grid-item-card}
:shadow: none
:class-card: sd-border-0

<div style="text-align: center;">
  <h4><strong>Ending Homelessness</strong></h4><br/>
</div>
We need to put people in homes now and ensure that everyone has a no-barrier pathway to economic security. Activists on the front lines of this effort have shown us the way forward: the Housing First approach. We have the power, and the responsibility, to make homelessness a thing of the past in Portland.
::::

::::{grid-item-card}
:shadow: none
:class-card: sd-border-0

<div style="text-align: center;">
  <h4><strong>Climate Resilience</strong></h4><br/>
</div>
The Gulf of Maine is warming more quickly than 99% of the world's oceans. Climate change poses an existential threat to coastal communities, and will drastically reshape our state if we do not act now. We must support a transition to clean energy, investments in resilience, and critical supports for the working waterfront.
::::

:::::

<hr class="rounded">

# Endorsements
<div style="text-align:center; margin-bottom:5%">I am honored to have the support of these grass-roots organizations.</div>

::::{grid} 1 3 3 3

:::{grid-item}
<!-- :class: endorsement-grid -->
[![afl_cio_logo](_static/endorsement_afl_cio_logo.png)](https://maineaflcio.org/)
:::

:::{grid-item}
<!-- :class: endorsement-grid -->
[![msea_logo](_static/endorsement_msea_logo.png)](https://mseaseiu.org/)
:::

:::{grid-item}
<!-- :class: endorsement-grid -->
[![mea_logo](_static/endorsement_mea_logo.png)](https://maineea.org/)
:::

:::{grid-item}
:columns: 6
:margin: 4 auto auto auto
:class: sd-border-0
<!-- :class: endorsement-grid -->
[![mpa_logo](_static/endorsement_mpa_logo.png)](https://mainepeoplesalliance.org/)
:::

:::{grid-item}
:columns: 6
:margin: 5 auto auto auto
:class: sd-border-0
<!-- :class: endorsement-grid -->
[![pp_pac_logo](_static/endorsement_pp_logo.png)](https://www.plannedparenthoodaction.org/planned-parenthood-maine-action-fund)
:::

::::

:::{toctree}
:maxdepth: 1
:hidden:

Issues<issues>
Updates<blog>
:::
