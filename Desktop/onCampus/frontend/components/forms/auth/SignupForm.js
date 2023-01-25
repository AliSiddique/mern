import { useForm } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from "yup";
import { useAppDispatch } from "../../../redux/store/store";
import { registerUser } from "../../../redux/slices/authSlice";
import { useRouter } from "next/router";

// register form validation with yup
const schema = yup.object().shape({
    username: yup.string().required(),
    email: yup.string().email().required(),
    password: yup.string().required(),
    password2: yup.string().required(),
});

export default function SignupForm() {
    // router
    const router = useRouter();
    // dispatch
    const dispatch = useAppDispatch();
    // form submit handler
    const onSubmit = (data) =>{
        dispatch(registerUser(data.username, data.email, data.password, data.password2))
    };
    // unpack useForm hook and pass in validation schema
const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema)
});
  return (
    <div>
        
        <form onSubmit={handleSubmit(onSubmit)}>
            <input {...register("username")} />
            <p>{errors.username?.message}</p>
                
            <input {...register("email")} />
            <p>{errors.email?.message}</p>

            <input type="password" {...register("password")
        } />
            <p>{errors.age?.message}</p>
            <input type="password" {...register("password2")} />
            <p>{errors.age?.message}</p>
            
            <input type="submit" />
            </form>
    </div>
  )
}
