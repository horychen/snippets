![[0cd9d6891c954e5dabf70a48caeb4d1.jpg]]
$\alpha$ and $\theta$ has connection:
$$
(d-ccos\theta-acos\alpha)^2+(asin\alpha-csin\theta)^2=b^2
$$
According to the definition of virtual work:
$$\delta W=\sum _{i}F_{i}\delta z_{i}+\sum _{j}M_{j}\delta \theta _{j}-\sum _{k}\dfrac{dV_{k}}{dq_{k}}\delta q_{k}$$
In this specific case, by letting $q=\theta$, we have  
$$\delta W=M_F\delta \theta+M\delta \theta-\dfrac{d}{d\theta}(V_{Ga}+V_{Gb}+V_{Gc}+V_{Gd})\delta \theta=0$$
where $M$ is the aim for virtual-work-analysis,
$$
M\delta\theta=\tau_B\frac{d\alpha}{d\theta}d\theta
$$
The direction of $\boldsymbol F$ is along the vector$\overrightarrow{OC}$, therefore
$$
F\delta z_{i}=\frac{d}{d\theta}(\frac{(d-ccos\theta-x_0,csin\theta-y_0)}{norm(OC)})\cdot(-sin\theta,-cos\theta)d\theta = M_F \delta\theta
$$

$\frac{d\alpha}{d\theta}$ can be calculated by implicitly deviation (derivation).

For the conservative forces (the derivative of the potential energy),
$$
\frac{d}{d\theta}V_{Ga}d\theta=\frac{d}{d\theta}\frac{G_a}{2}asin\alpha d\theta=\frac{aG_a}{2}cos\alpha\frac{d\alpha}{d\theta}d\theta
$$
$$
\frac{d}{d\theta}V_{Gb}d\theta=\frac{d}{d\theta}\frac{G_b}{2}(asin\alpha+csin\theta)d\theta=\frac{G_b}{2}(a\frac{d\alpha}{d\theta}cos\alpha+ccos\theta)d\theta
$$
$$
\frac{d}{d\theta}V_{Gc}d\theta=\frac{d}{d\theta}\frac{G_c}{2}csin\theta=\frac{cG_c}{2}cos\theta
$$
$$
\frac{d}{d\theta}V_{Gd}=0
$$

The aim of optimization is to get a smooth curve of moment or torque as well as get the max value of the torque.  The front-part of the condition is hard to describe by the loss function, but the other one is a minmax problem can be solved by fminmax in matlab as the paper said.
One of  the constrain condition is 
$$
l\leq s+p+q
$$ where l is the longest one, s, p and q are the rest of linkage. This is to make sure the structure will work as expected in the prospective of kinematic. Another constrain is the movable range of  B. The design of MIT's leg can have the range of 110 degrees.  The initial angle will be determined by the shape of shank. 

