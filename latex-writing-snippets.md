[Subequations](https://tex.stackexchange.com/questions/225517/subequations-with-main-equation-number)
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

Figure
```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=1\hsize]{image/pyx_sat_time_corr_annotated-crop.pdf}
  \caption{Graphical definitions of the symbols when $\rm Sat(\cdot)$ is introduced to VM.}
  \label{fig:GraphicalDefSatVM}
\end{figure}
```

Subfloats
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


[Table](https://www.tablesgenerator.com/latex_tables#)
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


Nomenclature (dedicated package)
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

Nomenclature (using what we have)
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

Nomenclature (IEEE native, my recommandation)
```latex
\section*{Nomenclature}
\begin{IEEEdescription}[\IEEEusemathlabelsep\IEEEsetlabelwidth{$Q_s,Q_r$}]
    \item[$p,p_s$ ] Number of pole pairs of torque and suspension winding, respectively.
    \item[$Q_s,Q_r$] Number of stator and rotor slots, respectively.
    \item[$\theta,\Omega$ ] Mechanical rotor position and speed, respectively.
    \item[$E_a,E_m$] Force error angle and magnitude, respectively.
\end{IEEEdescription}
```

negative space
```latex
    \newcommand{\ns}{\negthickspace\negthickspace\negthickspace\negthickspace\negthickspace\negthickspace}
```