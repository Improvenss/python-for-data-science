LINK: https://packaging.python.org/en/latest/tutorials/packaging-projects/
LINK: https://www.youtube.com/watch?v=Kz6IlDCyOUY&t=555s

shell commands {
    python3 -m venv venv
    source venv/bin/activate
    {
        (venv) yuandre@yuandre-macbook python-0-starting % pip list
            Package Version
            ------- -------
            pip     24.3.1
    }
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    python3 -m build
    {
        Successfully built ft_package-0.0.1.tar.gz and ft_package-0.0.1-py3-none-any.whl
        (venv) yuandre@yuandre-macbook ex09 % pip list
            Package         Version
            --------------- -----------
            build           1.2.2.post1
            packaging       24.2
            pip             24.3.1
            pyproject_hooks 1.2.0
    }
    pip install dist/ft_package-0.0.1.tar.gz
    {
        (venv) yuandre@yuandre-macbook ex09 % python
        Python 3.13.1 (main, Dec  3 2024, 17:59:52) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> count_in_list(["asdf", "abc"], "abc")
        Traceback (most recent call last):
        File "<python-input-0>", line 1, in <module>
            count_in_list(["asdf", "abc"], "abc")
            ^^^^^^^^^^^^^
        NameError: name 'count_in_list' is not defined
        >>> from ft_package import count_in_list
        >>> count_in_list(["asdf", "abc"], "abc")
        1
        >>>
    }
    pip install dist/ft_package-0.0.1-py3-none-any.whl --force-reinstall
    pip freeze > requirements.txt
    python3 -m pip install --upgrade twine

}