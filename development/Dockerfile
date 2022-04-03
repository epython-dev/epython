FROM pyodide/pyodide:0.19.1

# Switch shell to bash
SHELL ["/bin/bash", "--login", "-c"]

# Setup epyhton-dev
RUN mkdir -p /epython/ &&\
    mkdir -p /epython/epython/

# Copy Development Files
COPY ./development/environment.yaml .
COPY ./epython/* /epython/epython/
COPY setup.py /epython/
COPY README.md /epython/
COPY tests /epyhton/

# Install Miniconda
RUN wget --quiet "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh" -O ~/miniconda.sh &&\
/bin/bash ~/miniconda.sh -b -p /opt/conda &&\
/opt/conda/condabin/conda init bash 

ENV PATH /opt/conda/bin:/src/pyodide/:$PATH

# Activate environment, install epython
RUN conda env update -f ./environment.yaml
SHELL ["conda", "run", "-n", "epython-dev", "/bin/bash", "-c"]

RUN cd /epython/ && pip install .

CMD ["/bin/bash"]