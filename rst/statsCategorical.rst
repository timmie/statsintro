.. image:: ..\Images\title_categorical.png
    :height: 100 px

.. Tests on Categorical Data 
.. ==========================

In a sample of individuals the number falling into a particular group is
called the *frequency*, so the analysis of categorical data is the
analysis of frequencies. When two or more groups are compared the data
are often shown in the form of a *frequency table*, sometimes also
called *contingency table*.



+-------------+------------------+-----------------+-----------+
|             | *Right Handed*   | *Left Handed*   | *Total*   |
+=============+==================+=================+===========+
| *Males*     | 43               | 9               | 52        |
+-------------+------------------+-----------------+-----------+
| *Females*   | 44               | 4               | 48        |
+-------------+------------------+-----------------+-----------+
| *Total*     | 87               | 13              | 100       |
+-------------+------------------+-----------------+-----------+

If you have only one sample group of data, the analysis options are somewhat limited. In contrast, a number of statistical tests exist for the analysis of frequency tables.

Chi-square test
    This is the most common type. It is a hypothesis test, which checks if the entries in the individual cells all come from the same distribution. In other words, it checks if the results are independent of the row or column in which they appear.

Fisher's Exact Test
    While the chi-square test is approximate, the *Fisher's Exact Test* is an exact test. As it is computationally much more expensive and intricate than the chi-square test, it was originally used only for small sample numbers. However, in general it is now the more advisable test to use.

Cochran's Q Test
    This test, for which we will not go into detail here, is used if you have *matched/paired observations*. For example, if you have exactly the same samples analyzed by 3 different laboratories, and you want to check if the results are statistically equivalent, you would use this test.

McNemar's Test
    This is a matched pair test for 2x2 tables.


One Proportion 
---------------

If you have one sample group of data, you can check if your sample is
representative of the standard population. To do so, you have to know
the proportion :math:`p` of the characteristic in the standard
population. It can be shown that a in population with a characteristic
with probability :math:`p`, the standard error of samples with this
characteristic is given by

.. math:: se(p) = \sqrt{p(1-p)/n}

and the corresponding 95% confidence interval is

.. math:: ci = mean \pm se * t_{n,0.95}

If your data lie outside this confidence interval, they are *not*
representative of the population.

Frequency Tables
----------------

Chi-square Test
~~~~~~~~~~~~~~~

Assume you have observed absolute frequencies :math:`o_i` and expected
absolute frequencies :math:`e_i` under the Null hypothesis of your test
then it holds

.. math:: V = \sum_i \frac{(o_i-e_i)^2}{e_i} \approx \chi^2_f

.

where :math:`f` are the degrees of freedom. :math:`i` might denote a
simple index running from :math:`1,...,I` or even a multiindex
:math:`(i_1,...,i_p)` running from :math:`(1,...,1)` to
:math:`(I_1,...,I_p)`.

Assumptions
^^^^^^^^^^^^

The test statistic :math:`V` is approximately :math:`\chi^2`
distributed, if

-  for all absolute expected frequencies :math:`e_i` holds
   :math:`e_i \geq 1` and

-  for at least 80% of the absolute expected frequencies :math:`e_i`
   holds :math:`e_i \geq 5`.

For small sample numbers, corrections should be made for some bias that
is caused by the use of the continuous chi-squared distribution. This
correction is referred to as *Yates correction*.

Degrees of Freedom
^^^^^^^^^^^^^^^^^^

The degrees of freedom can be computed by the numbers of absolute observed
frequencies which can be chosen freely. For example, only one cell of a 2x2 table
with the sums at the side and bottom needs to be filled, and the others can be
found by subtraction. In general, an *r x c* table has *df=(r-1)x(c-1)*
degrees of freedom. We know that the sum of absolute expected frequencies is

.. math:: \sum_i o_i = n

which means that the maximum number of degrees of freedom is
:math:`I-1`. We might have to subtract from the number of degrees of
freedom the number of parameters we need to estimate from the sample,
since this implies further relationships between the observed
frequencies.

Example
^^^^^^^

The :math:`\chi^2` test can be used to generate "quick and dirty" test,
e.g.

:math:`H_0:` The random variable :math:`X` is symmetrically distributed
versus

:math:`H_1:` the random variable :math:`X` is not symmetrically
distributed.

We know that in case of a symmetrical distribution the arithmetic mean
:math:`\bar{x}` and median should be nearly the same. So a simple way to
test this hypothesis would be to count how many observations are less
than the mean (:math:`n_-`)and how many observations are larger than the
arithmetic mean (:math:`n_+`). If mean and median are the same than 50%
of the observation should smaller than the mean and 50% should be larger
than the mean. It holds

.. math:: V = \frac{(n_- - n/2)^2}{n/2} + \frac{(n_+ - n/2)^2}{n/2} \approx \chi^2_1

.

Comments
^^^^^^^^

The Chi-square test is a pure hypothesis test. It tells you if your
observed frequency can be due to a random sample selection from a single
population. A number of different expressions have been used for
chi-square tests, which are due to the original derivation of the
formulas (from the time before computers were pervasive). Expression
such as *2x2 tables*, *r-c tables*, or *Chi-square test of contingency*
all refer to frequency tables and are typically analyzed with chi-square
tests.

Fisher's Exact Test
~~~~~~~~~~~~~~~~~~~

If the requirement that 80% of cells should have expected values of at
least 5 is not fulfilled, *Fisher’s exact test* should be used. This
test is based on the observed row and column totals. The method consists
of evaluating the probability associated with all possible 2x2 tables
which have the same row and column totals as the observed data, making
the assumption that the null hypothesis (i.e. that the row and column
variables are unrelated) is true. In most cases, Fisher’s exact test is
preferable to the chi-square test. But until the advent of powerful
computers, it was not practical. You should use it up to approximately
10-15 cells in the frequency tables.

Analysis Programs
-----------------

With computers, the computational steps are trivial
(See also the ipython notebook `compGroups.ipynb <http://nbviewer.ipython.org/url/work.thaslwanter.at/Stats/ipynb/compGroups.ipynb>`_):

.. literalinclude:: ..\Code\compGroups.py

