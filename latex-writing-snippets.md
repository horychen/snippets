
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
%\setlist[description]{labelindent=25pt,style=multiline,leftmargin=2.5cm}
\setlist[description]{leftmargin=1.4cm, labelindent=0cm, labelsep=0.4cm, labelwidth=1.0cm}
\begin{description}
\item[$\hat ~,\tilde ~$] For derived symbols, $\hat ~$ and $\tilde ~$ stand for estimation and error quantities, respectively, e.g., $\tilde \alpha = \alpha-\hat \alpha$.
\item[$~^*$] An aster $~^\ast$ indicates the commanded quantities.
\item[$M$-$T$] The $M$-$T$ frame designates the rotor field oriented frame, where $M$-axis is aligned with the rotor flux vector while the $T$-axis is $90^\circ$ leading to the $M$-axis.
\item[$I,J$]
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

