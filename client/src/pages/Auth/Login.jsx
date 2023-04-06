import React from 'react';
import AuthForm from '../../components/AuthForm/AuthForm';
import styles from './Auth.module.scss';
import { useNavigate } from 'react-router-dom';
import axios from '../../axios';
import Cookie from 'js-cookie'


const Login = () => {


  const inputConfigs = [
    { title: "Адрес электронной почты", type: 'email', name: 'email' },
    { title: "Пароль", type: 'password', name: 'password' },
  ]

  const navigate = useNavigate()

  async function handleSubmit(e) {
    e.preventDefault();
    const email = e.target.email.value;
    const password = e.target.password.value;
    try {
      const response = await axios.post('/login', {
        email,
        password
      });

      Cookie.set('access_token', response.data.access_token);
      Cookie.set('refresh_token', response.data.refresh_token);
      Cookie.set('logged_in', true);
      Cookie.set('email', email)
      navigate('/home')
    } catch (error) {
      console.log(error.response.data.detail);
    }
  };

  return (
    <div className={styles.login}>
      <div className={`title ${styles.title}`}>Вход</div>
      <div className={styles.loginForm}>
        <AuthForm
          inputConfigs={inputConfigs}
          buttonTitle='Войти'
          authHelpText='Нет аккаунта?'
          onSubmit={handleSubmit}
          authHelpLink='Регистрация'
          link='/register'
        />
      </div>
    </div>
  )
};

export default Login;
