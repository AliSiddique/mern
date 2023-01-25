import { useForm } from "react-hook-form";
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from "yup";

const schema = yup.object().shape({
    email: yup.string().email().required(),
    password: yup.string().required(),
});
const onSubmit = (data) => console.log(data);
export default function LoginForm() {
   
const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema)
});
  return (
    <div>
        <form onSubmit={handleSubmit(onSubmit)}>
         
                
            <input {...register("email")} />
            <p>{errors.email?.message}</p>

            <input type="password" {...register("password")
        } />
            <p>{errors.password?.message}</p>
      
            
            <input type="submit" />
            </form>
    </div>
  )
}
