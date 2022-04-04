FROM pyodide/pyodide:0.19.1

# Switch shell to bash
SHELL ["/bin/bash", "-c"]

# Setup epyhton-dev
RUN mkdir -p /epython/ &&\
    mkdir -p /epython/epython/

# Copy Development Files
COPY ./development/environment.yaml .
COPY ./epython/* /epython/epython/
COPY setup.py /epython/
COPY README.md /epython/
COPY tests /epyhton/

# Add Conda to PATH
ENV PATH /opt/conda/bin:$PATH

# Install Miniconda
RUN wget --quiet "https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh" -O ~/miniconda.sh &&\
/bin/bash ~/miniconda.sh -q -b -p /opt/conda &&\
conda init &&\
conda env update --quiet -f ./environment.yaml &&\
echo "conda activate epython-dev" >> /root/.bashrc

ENV PATH /opt/conda/envs/epyhton-dev/bin:$PATH

SHELL ["conda", "run", "-n", "epython-dev", "/bin/bash", "-c"]

RUN cd /epython/ && pip install . &&\
    cd /src/pyodide/ && pip install -e pyodide-build

ENV PYTHONPATH /src/pyodide/pyodide-build/:$PYTHONPATH

RUN cd ./pyodide/ && make

CMD ["python", "-m", "pyodide_build", "serve"]