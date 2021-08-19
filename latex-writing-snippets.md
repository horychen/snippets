# Two separate figures side by side for double column space
```latex
\begin{figure*}
\centering
\begin{minipage}[t]{.66\textwidth}
        \subfloat[]{\!\!\!\!\!\!\!\!
            \includegraphics[width=0.495\hsize]{images/805-0700-slessinv-Vdc-2-crop-FontAsPath.pdf}
            \label{fig:varyVdc:a}
        }
        %\hspace{-0.5em}
        \subfloat[]{
            \includegraphics[width=0.505\hsize]{images/805-0700-slessinv-Vdc-4-crop-FontAsPath.pdf}
            \label{fig:varyVdc:b}
            \!\!\!\!\!
        }
        %\vspace{-1ex}
        \caption{Experimental sensorless operation with varying dc bus voltage.}
        \label{fig:varyVdc}
        %\vspace{-1ex}
\end{minipage}
%\qquad
\begin{minipage}[t]{.33\textwidth}
        \includegraphics[width=1\hsize]{images/805-0700-slessinv-load-2-crop-FontAsPath.pdf}
        %\vspace{-1ex}
        \caption{Experimental sensorless operation with varying load torque.}
        \label{fig:varyLoad}
        %\vspace{-1.5ex}
\end{minipage}
\end{figure*}
```

# Table with footnote

```latex
\usepackage{tikz, soul}
\newcommand*{\mycheckmark}[1][]{\tikz[x=1em, y=1em]\fill[#1] (0,.35) -- (.25,0) -- (1,.7) -- (.25,.15) -- cycle;}

\begin{table*}[t]
  \vspace{-1ex}
  \caption{Undesired Ingredients and Polar Plot Results \hl{What should caption be?}}
  \renewcommand{\arraystretch}{1.0}
  \scalebox{.95}
  {
        \centering
        \begin{tabular}{l|cccccc}
        \hline
        Design No.                             & 1   & 2   & 3   & 4    & 5   & 6   \\
        \hline
        \hline
        Harmonics at $h=p\pm1$                    & -$\!\!~^*$   & \mycheckmark$\!\!~^\dagger$ & \mycheckmark & \mycheckmark  & \mycheckmark & \mycheckmark \\
        Amplitude asymmetry in working harmonics $h=p_s$ & -   & -   & - & \mycheckmark  & \mycheckmark & -   \\
        Phase asymmetry in working harmonics $h=p_s$ & -   & -   & \mycheckmark & \mycheckmark  & \mycheckmark & -   \\
        Asymmetry in harmonics $h=p\pm1$       & -   & \mycheckmark   & \mycheckmark & \mycheckmark  & \mycheckmark & -   \\
        Elliptical force polar plot?              & No  & Yes   & Yes & Yes & Yes & No  \\
        Force difference in FPP, $\Delta F$ {[}N{]}                     & 0.06   & 5.6 & 9.4 & 27.5 & 5.3 & 0.27  \\
        $E_a$ variation in $E_a$ polar plot, $\Delta E_a$ [mech. deg] & 0.8   & 2.1   & 5.2  & 9.0   & 2.3  & 7.4 \\
        Acceptable Design? & Yes   & Yes  & No   & No    & Yes  & No \\
        \hline
        \end{tabular}
  }
  {
        \vspace{-2.0ex}
        \\
    \begin{flushleft}
            \begin{tabular}{l}
                \multicolumn{1}{l}{*Check mark ``\mycheckmark'' means the description applies.}\\
                \multicolumn{1}{l}{$\dagger$Dash ``-'' means the description does not apply.}
            \end{tabular}
    \end{flushleft}
  }
  \label{tab:ListOfIngredients}
\end{table*}
```

```latex
\begin{table}[t]
	\begin{minipage}{\columnwidth}
		%% increase table row spacing, adjust to taste
		\renewcommand{\arraystretch}{1.4}
		% if using array.sty, it might be a good idea to tweak the value of
		% \extrarowheight as needed to properly center the text within the cells
		\caption{Properties of Winding Types\cite{2009-Pyrhonen.Jokinen.ea-book-Designrotatingelectrical}.}
		\label{tab:FractionalSlotWinding}
		\centering
		%% Some packages, such as MDW tools, offer better commands for making tables
		%% than the plain LaTeX2e tabular which is used here.
		\scalebox{.8}{
			\begin{tabular}{c|cccc}\hline\hline
				& Integer-slot & First-grade & \multicolumn{2}{c}{Second grade}\\\hline
				% $Q'/m$ & ? & Even & \multicolumn{2}{c}{Odd} \\
				$t~\ra{\triangleq{\rm GCD}(Q,p)}$ & $p$ & $\frac{p}{n}$ & \multicolumn{2}{c}{$\frac{2p}{n}$} \\
				$n$ & $1$ & Odd & \multicolumn{2}{c}{Even} \\
				$180^\circ$ phasors?\footnote{whether the phasor star contains phasors in $180^\text{e}$ pairs} & Yes & Yes & \multicolumn{2}{c}{No} \\
				& & & Single layer & Double layer \\
				$Q^*$ & $Q'$ & $Q'$ & $2Q'$ & $Q'$ \\
				$p^*$ & $p'$ & $p'$ & $2p'$ & $p'$ \\ %\hline
		\end{tabular}}
	\end{minipage}
\end{table}
```

# Table with newline in a cell
Option 1:
```latex
\begin{table}[t]
	\begin{minipage}{\columnwidth}
		\renewcommand{\arraystretch}{1.4} %modify in conjunction with \extrarowheight to adjust row spacing
		\caption{Stator Winding Symmetry Requirements.}
		\label{tab:SymmetryRequirements}
		\centering
		\begin{tabular}{llc}\hline\hline
			%Winding & Requirement\\\hline
			%\multirow{2}{*}{1) Integer no. of coils per phase} & \vline {~~Single layer} & {Double layer} \\
          %& \vline ~~$\frac{p}{n} \in \mathbb{N} $ & $2\frac{p}{n} \in \mathbb{N}$ \\
			\multirow{2}{*}{1) Integer no. of coils per phase} & \multicolumn{1}{|c}{Single layer} & \multicolumn{1}{|l}{Double layer} \\
          & \multicolumn{1}{|c}{$\frac{p}{n} \in\mathbb{N}$} & \multicolumn{1}{|l}{$2\frac{p}{n} \in \mathbb{N}$} \\
         \hline
			2) Star of slots angular spacing  & \multicolumn{2}{|l}{$m$ and $n$ must be co-prime} \\
         %2) Star of slots angular spacing  & \vline \multicolumn{2}{c}{$m$ and $n$ must be co-prime} \\
% https://tex.stackexchange.com/questions/286922/misplaced-omit-multispan-omit
			% & & & & \\ \hline
       \hline
       \vspace{-3.5ex}
       \\
%       \multicolumn{3}{l}{Note: $m$ is phase number, $p$ is pole pair number, and $n$ is \hl{den of $q$?}.}\\
%       \multicolumn{3}{l}{$n$ is \hl{??? (n is harmonic order in this paper already)}}
		\end{tabular}
	\end{minipage}
\end{table}
```

Option 2:
IEMDC 2019 paper

# Extra { bug can de deadly
```latex
%令人绝望的bug（无法debug）：
\multicolumn{7}{l}{*{*The phase angles of $\bar {\boldsymbol{k}}_{Sw}(4)$ of the three phases are 0, 110, -140 $\rm [elec.deg]$.}

%正确
\multicolumn{7}{l}{*The phase angles of $\bar {\boldsymbol{k}}_{Sw}(4)$ of the three phases are 0, 110, -140 $\rm [elec.deg]$.}

```

# Latexmk command that I used
```
latexmk -quiet -pdf -synctex=1 -pvc -view=none -jobname=./aux-files/ismb2021 ismb2021
del pdflatex*.fls
```

#### Some details about math notations
% 转置符号不是T
```
\newcommand{\transpose}{^\mathsf{T}}
%$\mathbf{A}^\mathrm{T}$
%$\mathbf{A}^\top$
%$\mathbf{A}^\mathsf{T}$
%$\mathbf{A}^\intercal$
```

% 微分符号不是d

#### New line in Table Row
My IEMDC 2019 paper
```latex
% for using new line in table
\usepackage{makecell}
\renewcommand\theadalign{bc}
\renewcommand\theadfont{\bfseries}
\renewcommand\theadgape{\Gape[4pt]}
\renewcommand\cellgape{\Gape[4pt]}
```

#### thank note as footnote
```latex
\newcommand\blfootnote[1]{%
  \begingroup
  \renewcommand\thefootnote{}\footnote{#1}%
  \addtocounter{footnote}{-1}%
  \endgroup
}
```

#### Todo and Revision
% For Revision
```
\usepackage[final]{changes} % it clears the traces of changes made by the authors and respecting the last changes.
\usepackage[markup=underlined]{changes}
\definechangesauthor[name={Jiahao Chen}, color=blue]{CJH}
\definechangesauthor[name={Eric Loren Severson}, color=orange]{ELS}
```

% Simple Revision
```
 \definecolor{darkgreenOri}{RGB}{84, 139, 34}
 \definecolor{sthlmRedOri}{RGB}{196,0,100}
 \definecolor{ranewRedOri}{RGB}{220,0,120}
 \definecolor{darkBlueOri}{RGB}{15,40,127}
 \definecolor{sthlmBlueOri}{RGB}{0,110,191}
\newcommand{\idraft}[1]{#1} %{\textcolor{darkgreen}{#1}}
\newcommand{\ra}[1]{\textcolor{sthlmRed}{#1}}
\newcommand{\ranew}[1]{\textcolor{ranewRed}{#1}}
\newcommand{\ecce}[1]{#1} %{\textcolor{darkBlue}{#1}}
\newcommand{\rb}[1]{\textcolor{sthlmBlue}{#1}}
```

% Todo Notes
```
\usepackage[colorinlistoftodos,prependcaption,textsize=small]{todonotes}
%\usepackage[disable]{todonotes}
\newcommand{\todoINFO}[1]{\todo[inline, color=blue!25]{INFO: #1}}
\newcommand{\todoIMPORTANT}[1]{\todo[inline, color=red!25]{IMPORTANT: #1}}
\newcommand{\todoREVA}[1]{\todo[inline, color=green!25]{REVISED: #1}}
```


#### 取消文末对齐
注释掉 IEEE 提供的模板的这一句：
```
%\usepackage{flushend}
```

#### Table of Figures
Instead of 
```latex
\begin{figure*}[t]
    \centering
    \vspace{-2ex}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=05_(a).png}\label{fig16-kb05-a}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=05_(b).png}\label{fig16-kb05-b}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=05_(c).png}\label{fig16-kb05-c}}

    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=10_(a).png}\label{fig16-kb10-a}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=10_(b).png}\label{fig16-kb10-b}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=10_(c).png}\label{fig16-kb10-c}}

    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=20_(a).png}\label{fig16-kb20-a}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=20_(b).png}\label{fig16-kb20-b}}
    \subfloat[]{\includegraphics[width=.4\columnwidth]{Figures/Fig16_kb=20_(c).png}\label{fig16-kb20-c}}
    \caption{Tracking performance of the three systems for step speed reference under different $k_b$.}
    \label{fig16}
    \vspace{-3ex}
\end{figure*}
```
Let's do this:
```latex
%\begin{table*}
\begin{figure*}
    \centering
    %\begin{tabular}{cccc}
    %\begin{tabular}{cM{20mm}M{20mm}M{20mm}}
    %\begin{tabular}{c@{\hspace{1mm}}M{20mm}M{20mm}M{20mm}}
    \begin{tabular}{c@{\hspace{-0.0em}}M{.55\columnwidth}M{.55\columnwidth}M{.55\columnwidth}}
       \toprule
        $k_b$ & $\rm 3^{rd}ESO\_1$ & $\rm 3^{rd}ESO\_4$ & $\rm 4^{th}ESO\_1$ \\
        \midrule
        0.5 & \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=05_(a).png}\label{fig16-kb05-a} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=10_(a).png}\label{fig16-kb10-a} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=20_(a).png}\label{fig16-kb20-a} \\
        1.0 & \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=05_(b).png}\label{fig16-kb05-b} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=10_(b).png}\label{fig16-kb10-b} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=20_(b).png}\label{fig16-kb20-b} \\
        2.0 & \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=05_(c).png}\label{fig16-kb05-c} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=10_(c).png}\label{fig16-kb10-c} &
              \includegraphics[width=.55\columnwidth]{Figures/Fig16_kb=20_(c).png}\label{fig16-kb20-c} \\
        \bottomrule
    \end{tabular}
    \caption{Tracking performance of the three systems for step speed reference under different $k_b$.}
    \label{tbl:table_of_figures}
%\end{table*}
\end{figure*}
```

#### [Text Column in Array](https://tex.stackexchange.com/questions/62902/text-column-in-array)
```
\usepackage{array,amsmath}
\newcolumntype{L}{>$l<$}

	\begin{array}{L@{\quad}c@{{}={}}c}
       some text:            & x^2 & x^2 \\
       more thoughts:        & y^2 & y^2 \\
       really deep thoughts: & z^2 & z^2
    \end{array}
```
	

#### [Variant of Capital Geek Variable](https://tex.stackexchange.com/questions/87238/greek-letters-in-italic-in-math-equation)
```
\usepackage{amsmath}

\let\Gamma\varGamma
\let\Delta\varDelta
\let\Theta\varTheta
\let\Lambda\varLambda
\let\Xi\varXi
\let\Pi\varPi
\let\Sigma\varSigma
\let\Upsilon\varUpsilon
\let\Phi\varPhi
\let\Psi\varPsi
\let\Omega\varOmega
```

#### Bold Math

To be used inside math environment, \bm is more professional than \boldsymbol. Refer to:
> https://latex.org/forum/viewtopic.php?t=26738

To be used outside of math environment, consider to try the declration command \boldmath$\chi=Je$
> https://www.giss.nasa.gov/tools/latex/boldmath.html

Method 1:
```latex
\mbox{
	\boldmath
	$$math formaula$$
}
```

Method 2:
```latex
\boldmath
	$$math formaula$$
\unboldmath
```


#### [Subequations](https://tex.stackexchange.com/questions/225517/subequations-with-main-equation-number)
```latex
\begin{subequations}\label{eq:CLEST:main}
\begin{align}
	p\left( \psi _2+L_{\sigma}i_s \right) &=\mathrm{emf}+\left( k_p+\frac{k_i}{p} \right) \left( L_{\sigma}i_s-\hat{\psi}_{\sigma} \right) \label{eq:clest:a}\\
	p\hat{\psi}_{d\mu}&=-\alpha \hat{\psi}_{d\mu}+r_{\mathrm{req}}\left( i_{\alpha s}\cos \hat{\rho}+i_{\beta s}\sin \hat{\rho} \right) \label{eq:clest:b}\\
	\hat{\psi}_{\sigma}&=\left[ \begin{array}{c}
	\hat{\psi}_{\alpha \sigma}\\
	\hat{\psi}_{\beta \sigma}\\
\end{array} \right] =\left[ \begin{array}{c}
	\psi _{\alpha 1}-\hat{\psi}_{d\mu}\cos \hat{\rho}\\
	\psi _{\beta 1}-\hat{\psi}_{d\mu}\sin \hat{\rho}\\
\end{array} \right] \label{eq:clest:c}
\end{align}
\end{subequations}
```

#### Figure Option 1
```latex
\renewcommand{\figlocation}{images/AC-Force-Test-SC+PS-crop.pdf}
\renewcommand{\figname}{Measured AC force versus slip frequency characteristics of both pole-specific rotor and squirrel cage rotor prototypes at standstill.}
\renewcommand{\figlabel}{fig:ACForceVersusSlip}
\begin{figure}[t]
    \centering
    \includegraphics[scale=0.4]{\figlocation}
    \vspace{-2ex}
    \caption{\figname}
    \label{\figlabel}
    \vspace{-2ex}
\end{figure}
```

#### Figure Option 2
```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=1\hsize]{image/pyx_sat_time_corr_annotated-crop.pdf}
  \caption{Graphical definitions of the symbols when $\rm Sat(\cdot)$ is introduced to VM.}
  \label{fig:GraphicalDefSatVM}
\end{figure}
```

#### Subfloats Option 1
```latex
\renewcommand{\figAlocation}{images/EXP-BLOCKED-TORQUE-VERSUS-SLIP-crop.pdf}
\renewcommand{\figBlocation}{images/EXP-BLOCKED-TORQUE-VERSUS-SLIP-SUSPENSION-REGULATION-crop.pdf}
\renewcommand{\figAsubcap}{Torque Regulation}
\renewcommand{\figBsubcap}{Suspension Regulation}
\renewcommand{\figAlabel}{fig:TorqueVersusSlip}
\renewcommand{\figBlabel}{fig:TorqueVersusSlipSusReg}
\renewcommand{\figname}{Measured torque versus slip frequency characteristics from  (a) torque terminals, and (b) suspension terminals, of both pole-specific rotor and squirrel cage rotor prototypes at standstill.}
\renewcommand{\figlabel}{fig:TorqueTest}
\begin{figure}[t]
    \centering
    \subfloat[\figAsubcap]{\includegraphics[scale=0.395]{\figAlocation}\label{\figAlabel}}
    \hspace{-0ex}
    \subfloat[\figBsubcap]{\includegraphics[scale=0.395]{\figBlocation}\label{\figBlabel}}
    \vspace{-1ex}
    \caption{\figname}
    \label{\figlabel}
    \vspace{-2.5ex}
\end{figure}
```

#### Subfloats Option 2
```latex
\begin{figure}[t]
    \centering
    \subfloat[Experimental test stand]{
    \begin{tikzpicture}[>=stealth]
	    \node[anchor=south west,inner sep=0] (image) at (0, 0) {\includegraphics[width=0.4\columnwidth]{images/MachineInMill.jpg} };
	    \draw[->, green, ultra thick] (2.75,.41) node[below,font = \footnotesize]{\textbf{Load cell}} -- (2,.65);
	    \draw[->, green, ultra thick] (2.65,2.15) node[above,font = \footnotesize]{\textbf{Stator}} -- (2.3,1.75);
	    \draw[->, green, ultra thick] (1.1,2.75) node[above,align = center, font = \footnotesize]{\textbf{Mill head} \\ \textbf{and rotor}} -- (1.65,2.35);
	\end{tikzpicture} \label{fig:BearinglessTeststand}
	}
    \subfloat[Stator winding connections]{\includegraphics[scale=0.67]{images/ParallelWindingConnections.pdf} \label{fig:driveConnections}}
    \caption{(a) CNC mill configured for use as a bearingless motor test stand; (b) Winding connections for parallel no voltage winding.}
    \vspace{-3ex}
\end{figure}
```


#### [Table](https://www.tablesgenerator.com/latex_tables#)
```latex
\begin{table}[!t]
  \caption{List of All Reviewed Flux Estimators}
  \centering
  \renewcommand{\arraystretch}{1.2} % increase vertical space for each row
  \small\addtolength{\tabcolsep}{-3.5pt}
  \scalebox{.9}{
    \begin{tabular}{lccccc}
    \hline\hline
    & \multicolumn{1}{c}{\begin{tabular}[c]{@{}c@{}}Flux cmd.\\ dependency\end{tabular}}
    &                    \begin{tabular}[c]{@{}l@{}}Field angle\\ dependency\end{tabular}
    &                    \begin{tabular}[c]{@{}l@{}}Flux control\\ disturbance?\end{tabular}
    &                    \begin{tabular}[c]{@{}l@{}}Steady state\\ assumption?\end{tabular}
    &                    \begin{tabular}[c]{@{}l@{}}Performance\\ assessment\end{tabular} \\
    \hline
    Ohtani (1990)       & $\psi^*$  & $\rho^*$    & Yes  &  Yes & Bad \\
    Holtz (2002)        & $\psi^*$  & $\hat\rho$  & Yes  &  Yes & Bad \\
    Lascu (2006)        & $\psi^*$  & $\hat\rho$  & Yes  &  Yes & Bad \\
    PI Correction       & $\psi^*$  & $\rho^*$    & Yes  &  Yes & Bad \\ \hline
    Hu (1998)           & -         & $\hat\rho$  &  No  &  Yes & Bad \\
    Stoji{\'c} (2015)   & -         & -           &  No  &  Yes & Bad \\
    SCVM                & -         & -           &  No  &  Yes & Bad \\
    Holtz (2003)        & -         & -           &  No  &  Yes & Bad \\
    Adaptive Limit      & -         & -           &  No  &   No & Bad \\
    Closed Loop         & -         & $\hat\rho$  &  No  &   No & Bad \\
    \hline
    \end{tabular}
    }
  \label{tab:ListOfFluxEst}      % is used to refer this table in the text
\vspace{-2ex}
\end{table}
```


#### Nomenclature 1 (dedicated package)
```latex
% 系统命名法：https://www.overleaf.com/learn/latex/nomenclatures
\usepackage{nomencl}
\makenomenclature
\nomenclature{$\psi^*$}{Rotor flux (linkage) modulus command, equal to $0.7~\mathrm{Wb}$ in this paper.}
\nomenclature{$\rho*$}{Commanded rotor field angular position, a.k.a., current model field angular position.}
\printnomenclature
% need extra compile tool: https://tex.stackexchange.com/questions/62061/problem-with-the-nomenclature
%makeindex test.nlo -s nomencl.ist -o test.nls
% or:
%pdflatex n.tex
%makeindex n.nlo -s nomencl.ist -o n.nls
%pdflatex n.tex
```

#### Nomenclature 2 (using what we have)
```latex
\usepackage{enumitem}% http://ctan.org/pkg/enumitem, for \setlist
%\setlist[description]{labelindent=25pt,style=multiline,leftmargin=2.5cm}
\setlist[description]{leftmargin=1.4cm, labelindent=0cm, labelsep=0.4cm, labelwidth=1.0cm}
\begin{description}
\item[$\hat ~,\tilde ~$] For derived symbols, $\hat ~$ and $\tilde ~$ stand for estimation and error quantities, respectively, e.g., $\tilde \alpha = \alpha-\hat \alpha$.
\item[$~^*$] An aster $~^\ast$ indicates the commanded quantities.
\item[$M$-$T$] The $M$-$T$ frame designates the rotor field oriented frame, where $M$-axis is aligned with the rotor flux vector while the $T$-axis is $90^\circ$ leading to the $M$-axis.
\end{description}
```

#### Nomenclature 3 (IEEE native, my recommandation)
```latex
\section*{Nomenclature}
\begin{IEEEdescription}[\IEEEusemathlabelsep\IEEEsetlabelwidth{$Q_s,Q_r$}]
    \item[$p,p_s$ ] Number of pole pairs of torque and suspension winding, respectively.
    \item[$Q_s,Q_r$] Number of stator and rotor slots, respectively.
    \item[$\theta,\Omega$ ] Mechanical rotor position and speed, respectively.
    \item[$E_a,E_m$] Force error angle and magnitude, respectively.
\end{IEEEdescription}
```

#### Negative space
```latex
	\! = negative \,
    \newcommand{\ns}{\negthickspace\negthickspace\negthickspace\negthickspace\negthickspace\negthickspace}
```

#### em and ex
Please note that `em` is preferably used in horizontal measurements and `ex` in vertical measurements.
> https://tex.stackexchange.com/questions/338435/how-to-reduce-space-between-end-of-table-and-footnote-using-parnote


#### Parnotes (footnote for table)
> https://tex.stackexchange.com/questions/338435/how-to-reduce-space-between-end-of-table-and-footnote-using-parnote

